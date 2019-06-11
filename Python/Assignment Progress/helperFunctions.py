import pygame as pg
from colours import *
import os
import pickle
from AssignmentProgress import events
from datetime import datetime, timedelta

message_font = pg.font.SysFont('Calibri', 40)

def message(message, surface):
    text = message_font.render(message,0,WHITE)
    message_rect = (0,805,1190,45)
    #draw over the text that was there before
    surface.blit(text, (5,810))
    pg.display.update(message_rect)
    # pg.display.update()
    events()
    pg.draw.rect(surface, BLACK, message_rect)
    pg.display.update(message_rect)
    # pg.display.update()

def removeAssignment(surface, click_spots, page, page_1_sprites):
    message_rect = (0,805,1190,45)

    text1 = message_font.render("Single click on an assignment to select it",0,WHITE)
    #draw over the text that was there before
    surface.blit(text1, (5,810))
    pg.display.update(message_rect)

    #returns a number from 0 to 7 corresponding to the assignment that was clicked
    asn_num = events(click_spots,False)
    sprites = page_1_sprites.sprites()
    selected_sprite_title = sprites[asn_num*(page+1)].assignment.title
    
    pg.draw.rect(surface, BLACK, message_rect)
    text1 = message_font.render("Remove '{}'? Click on it again".format(selected_sprite_title),0,WHITE)
    surface.blit(text1, (5,810))
    pg.display.update(message_rect)

    #returns a number from 0 to 7
    asn_num2 = events(click_spots)

    #remove the assignment
    if asn_num == asn_num2:
        pkl_assignments = loadSort()
        pkl_assignments.pop(asn_num*(page+1))
        os.remove("assignments.pkl")
        for i in range(len(pkl_assignments)):
            save_object(pkl_assignments[i])

    pg.draw.rect(surface, BLACK, message_rect)
    pg.display.update(message_rect)
    # pg.display.update()    

def getDuedateBackground(assignment):
    #checks if an assignment is due soon
    #Black > week
    #green > 3 days
    #yellow > 1 day
    #red < 1 day
    #flashing red < 1 hr
    due_date = assignment.due_date
    now = datetime.now()
    diff = due_date - now
    assignment.time_left = str(diff)[:-7]
    if diff > timedelta(weeks=1):
        # print('due_date:', due_date)
        background = BLACK
    elif diff > timedelta(days=3):
        background = GREEN
    elif diff > timedelta(days=1):
        background = YELLOW
    elif timedelta(0) <= diff < timedelta(days=1):
        background = RED
    else:
        background = WHITE
    return background

def new_line(text):
    if len(text) > 40:
        line_0 = text[:39]+"-$_$"
        line_1 = text[39:]
        return line_0 + new_line(line_1)
    return text

def string2date(date):
    #an error will be raised if the date was formatted incorrectly
    try:
        # due date format 2019-06-05T25:53
        #remove spaces in the date
        if " " in date:
            date.replace(" ","")
        #if only the date was given, default to a time fo 23:59
        if "T" not in date:
            t = ['23','59']
            d = date.split('-')
        else:
            d_t = date.split('T')
            t = d_t[1].split(':')
            d = d_t[0].split('-')
        due = datetime(int(d[0]),int(d[1]),int(d[2]),int(t[0]),int(t[1]))
        #checks if the datetime given is prior to the current datetime
        if due < datetime.now():
            #This will be processed as an error
            return 0
        return due
    except:
        return False

def drawScreen(surface):
    #black background
    pg.draw.rect(surface, BLACK, (0,0,1200,800), 0)

    #yellow lines
    for i in range(3):
        x_pos = 300*(i+1)
        pg.draw.line(surface, YELLOW, (x_pos,0), (x_pos,800), 2)
    pg.draw.line(surface, YELLOW, (0,400), (1200,400), 2)

def drawPageNumber(surface,page):
    #page number
    pg.draw.rect(surface, BLACK, (1208,810,42,40),0)
    page_text = message_font.render(str(page), True, WHITE)
    surface.blit(page_text, (1208,810))

def rect2start_pos(rect):
    #(left, top, width, height) => (x1,y1),(x2,y2)
    x1 = rect[0]
    y1 = rect[1]
    return (x1,y1)

def rect2end_pos(rect):
    #(left, top, width, height) => (x1,y1),(x2,y2)
    x2 = rect[0] + rect[2]
    y2 = rect[1] + rect[3]
    return (x2,y2)

def pair2rect():
    #(x1,y1),(x2,y2) => (left, top, width, height)
    pass

def loadSort():
    #loads the assignmets
    assignments = [i for i in loadall()]
    #sorts the assignements
    sortKey = lambda ans : ans.due_date
    assignments.sort(key=sortKey)
    return assignments

def save_object(obj, filename="assignments.pkl"):
    with open(filename, 'a+b') as output:  # Appends to the file
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def loadall():
    if not os.path.exists('assignments.pkl'):
        open('assignments.pkl', 'a').close()
    if os.path.getsize('assignments.pkl') > 0:
        #display assignmets 1-8
        with open('assignments.pkl', "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break