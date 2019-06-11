#William Losin
#June 6, 2019

import pygame as pg
import sys
import os

from helperClasses import *
from colours import *
from helperFunctions import *


global surface

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

#RECT
# (left,top,width, height)

#width and height of surface
(w, h) = (1250,850)

#surface initialization
surface = pg.display.set_mode((w, h))#, pg.RESIZABLE)
pg.display.set_caption('Pygame Test')
surface.fill(BLACK)

#font
pg.font.init()
message_font = pg.font.SysFont('Calibri', 40)
general_font = pg.font.SysFont('Calibri', 14)


def preparation():    
    #message box
    #the message box does not extend into the main (1200,850) area
    #stretches from y=800 to 804
    pg.draw.line(surface, WHITE, (0,802),(w,802),5)

    #box areas
    # 0,1,2,3
    # 4,5,6,7
    #Because of the dividing line, each box loses one or two pixels
    boxes_rect = [
        (0  ,0,  299,399),
        (301,0,  298,399),
        (601,0,  298,399),
        (901,0,  298,399),
        (0  ,401,299,398),
        (301,401,298,398),
        (601,401,298,398),
        (901,401,298,398),
    ] 

    ########################## INITIAL GRAPHICS ###############################
    #navigation bar (on the right, 50 pixels allocated)
    #stretches from x=1200 to 1204
    #because of the domain, the rects are confined to 46x46
    pg.draw.line(surface, WHITE, (1202,0),(1202,h),5)
    #next page
    next_page_rect = (1205,0,45,45)
    pg.draw.lines(surface, WHITE, True, [(1214,30),(1227,12),(1240,30)], 3)
    pg.draw.lines(surface, RED, True, [(1216,29),(1229,11),(1242,29)], 3)
    #previous page
    prev_page_rect = (1205,46,45,45)
    pg.draw.lines(surface, WHITE, True, [(1214,58),(1227,76),(1240,58)], 3)
    pg.draw.lines(surface, RED, True, [(1216,57),(1229,75),(1242,57)], 3)
    #undo
    undo_rect = (1205,92,45,45)
    pg.draw.arc(surface, WHITE, (1216,102,26,26), -3.14159/2, 3.14159, 3) 
    pg.draw.lines(surface, WHITE, False, [(1212,110),(1218,117),(1224,110)], 3)
    pg.draw.arc(surface, RED, (1218,101,26,26), -3.14159/2, 3.14159, 2) 
    pg.draw.lines(surface, RED, False, [(1214,109),(1220,116),(1226,109)], 3)
    #redo
    redo_rect = (1205,138,45,45)
    pg.draw.arc(surface, WHITE, (1214,148,26,26), 0, 3/2*3.14159, 3) 
    pg.draw.lines(surface, WHITE, False, [(1232,156),(1238,163),(1242,156)], 3)
    pg.draw.arc(surface, RED, (1216,147,26,26), 0, 3/2*3.14159, 2) 
    pg.draw.lines(surface, RED, False, [(1234,155),(1240,162),(1244,155)], 3)
    #add assignment
    add_rect = (1205,184,45,45)
    pg.draw.line(surface, WHITE, (1214,207),(1240,207),3)
    pg.draw.line(surface, WHITE, (1227,194),(1227,220),3)
    pg.draw.line(surface, RED, (1216,206),(1242,206),3)
    pg.draw.line(surface, RED, (1229,193),(1229,219),3)
    #remove assignment
    remove_rect = (1205,230,45,45)
    pg.draw.line(surface, WHITE, (1214,253),(1240,253),3)
    pg.draw.line(surface, RED, (1216,252),(1242,252),3)


    #page number
    page_num_rect = (1205,805,45,45)

    # pg.draw.line(surface, RED, (0,400), (0,400), 1)
    # pg.draw.line(surface, RED, (1200,100), (1200,100), 1)

    #pg.display.flip()
    #############################################################################

    buttons_rect = [next_page_rect,prev_page_rect,undo_rect,redo_rect,add_rect,remove_rect]
    visuals_rect = [boxes_rect,page_num_rect]

    return buttons_rect, visuals_rect

def events(clickables=[(0,0,w,h)], timer_on=True):
    # ticks = 0
    timer = pg.USEREVENT+1
    pg.time.set_timer(timer, 1000)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == timer and timer_on:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                for i in range(len(clickables)):
                    boundary_rect = pg.Rect(clickables[i])
                    if boundary_rect.collidepoint(event.pos):
                        return i

def popup_events(input_boxes, popup_buttons, popup_sprites):
    popup_sprite = popup_sprites.sprites()[0]
    #image = popup_sprite.image

  
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONUP:
                for i in range(len(popup_buttons)):
                    boundary_rect = pg.Rect(popup_buttons[i])
                    if boundary_rect.collidepoint(event.pos):
                        if i == 0:
                            #remove the text in the text boxes
                            for box in input_boxes:
                                box.clear_text()
                            #exit add attachment window
                            running = False

                        if i == 1:
                            #submit the assignment
                            add_assignment_data = [popup_sprite.input_boxes[i].text for i in range(5)]
                            #checks if there is a title and a due date                            
                            if add_assignment_data[0] != '' and add_assignment_data[2] != '':
                                asn = Assignment(add_assignment_data[0],
                                                 add_assignment_data[2],
                                                 add_assignment_data[1],
                                                 add_assignment_data[3],
                                                 add_assignment_data[4],
                                                )
                                #checks if the inputted date was formatted properly
                                if asn.due_date == False:
                                    message("Error: improper date fromatting (use YYYY-MM-DDTHH:mm)", surface)
                                elif asn.due_date == 0:
                                    message("The due date cannot be sonner than right now", surface)
                                else:
                                    #saved to "assignments.pkl"
                                    save_object(asn)
                                    message("Added assignment '{}'".format(add_assignment_data[0]),surface)
                                    #remove the text in the text boxes
                                    for box in input_boxes:
                                        box.clear_text()
                            else:
                                message("The assignement is missing a title or a due date.",surface)
                            running = False


            for i in range(len(input_boxes)):
                if i>0 and input_boxes[i-1].next_tab:
                    input_boxes[i].tab = True
                inp = input_boxes[i].handle_event(event)
                if inp == 1:
                    break
                if i>0 and input_boxes[i-1].next_tab:
                    input_boxes[i-1].next_tab = False
                    break

        for box in input_boxes:
            box.update()
           
        popup_sprites.draw(surface)
        popup_sprites.update(surface)
        for box in input_boxes:
            box.draw(surface)
        
        pg.display.flip()

def reload_asn(page_1_sprites, boxes_rect, page):
    #returns assignements sorted by due date
    assignments = loadSort()
    #empties the sprite group
    page_1_sprites.empty()
    #display assignments on the screen  
    for i in range(page*8,len(assignments)):
        if i < 8*(1+page):
            #chacks if the background colour needs to change
            background = getDuedateBackground(assignments[i])
            asn = DisplayAssignment((boxes_rect[i%8][0],boxes_rect[i%8][0]),boxes_rect[i%8],assignments[i],background)
            page_1_sprites.add(asn)

    drawScreen(surface)
    page_1_sprites.update(surface)  

def pageUp(page):
    #only goes up a page if there are assignments on it
    #loads the assignmets
    assignments = [i for i in loadall()]
    if len(assignments) > (page+1)*8:
        page += 1
    return page

def pageDown(page):
    if page != 0:
        page -= 1
    return page

def main():
    buttons_rect, visuals_rect = preparation()

    #initial page number
    page = 0
    
    drawScreen(surface)
    drawPageNumber(surface,page)

    popup_rect = pg.Rect(400,150,400,500)

    add_attachment_popup = Popup((400,500),popup_rect)
    popup_sprites = pg.sprite.Group(add_attachment_popup)
    popup_buttons = [add_attachment_popup.exit_win_rect, add_attachment_popup.submit_rect]

    page_1_sprites = pg.sprite.Group()

    # all_sprites = pg.sprite.Group()

    reload_asn(page_1_sprites, visuals_rect[0], page)

    pg.display.update()

    while True:
        button_clicked = events(buttons_rect)
        # print("button clicked: ", button_clicked)
        if button_clicked == 0:
            #next_page
            page = pageUp(page)
        elif button_clicked == 1:
            #prev_page
            page = pageDown(page)
        elif button_clicked == 2:
            #undo
            pass
        elif button_clicked == 3:
            #redo
            pass
        elif button_clicked == 4: 
            #copy the rect that will be filled
            sub = surface.subsurface(popup_rect)
            sub = sub.copy()
            #add assignment popup
            popup_events(add_attachment_popup.input_boxes, popup_buttons, popup_sprites) 
            #paste the copied rect to return to the main screen
            surface.blit(sub, (popup_rect.x,popup_rect.y))    
        elif button_clicked == 5:
            #remove assignment
            removeAssignment(surface, visuals_rect[0], page, page_1_sprites)         
        else:    
            pass
            #print("here")
        #print(page)

        drawPageNumber(surface,page)
        reload_asn(page_1_sprites, visuals_rect[0], page)  
        pg.display.update()

if __name__ == '__main__':
    main()