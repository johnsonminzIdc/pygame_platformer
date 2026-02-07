import pygame

def user_intent(event):
    keys=pygame.key.get_pressed()
    input_data={"x-axis":0,"y-axis":0,"jump":False,"attack":False}
    if keys[pygame.K_UP]:
        input_data["y-axis"]= -1
    if keys[pygame.K_DOWN]:
        input_data["y-axis"]= 1
    if keys[pygame.K_RIGHT]:
        input_data["x-axis"]= 1
    if keys[pygame.K_LEFT]:
        input_data["x-axis"] = -1
        
    for events in event:
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE and not input_data["jump"] ==True:
                input_data["jump"]= True
            if events.key == pygame.K_v and not input_data["attack"]== True:
                input_data["attack"] = True
    
    return input_data
        