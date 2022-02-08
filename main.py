import arcade

def main():
    #=#=#=#=# Create the Window #=#=#=#=#
    arcade.open_window(1400,1200, "The Race Track")
    arcade.set_background_color(arcade.color.APPLE_GREEN)
    extra_grass = arcade.create_rectangle(475, 1045, 1850, 129, arcade.color.APPLE_GREEN)
    road = arcade.create_rectangle(475, 800, 1850, 495, arcade.color.GRAY)

    #=#=##=#=#Finish line parts#=#=#=#=#
    flp1 = arcade.create_rectangle(1350, 800, 250, 493, arcade.color.WHITE)
    flp2 = arcade.create_rectangle(1360, 865, 90, 90, arcade.color. BLACK)
    flp3 = arcade.create_rectangle(1270, 955, 90, 90, arcade.color. BLACK)
    flp4 = arcade.create_rectangle(1270, 777, 90, 90, arcade.color. BLACK)
    flp5 = arcade.create_rectangle(1270, 598, 90, 90, arcade.color. BLACK)
    flp6 = arcade.create_rectangle(1360, 687, 90, 90, arcade.color. BLACK)



    #=#=#=#=# Road Dividers #=#+#+#=#
    road_divider = arcade.create_rectangle(475, 800, 100, 10, arcade.color.YELLOW)
    road_divider2 = arcade.create_rectangle(785, 800, 100, 10, arcade.color.YELLOW)
    road_divider3 = arcade.create_rectangle(1100, 800, 100, 10, arcade.color.YELLOW)

    #=#=#=#=# Sky #=#=#=#=#
    sky = arcade.create_rectangle(475, 1150, 2000, 100, arcade.color.BABY_BLUE)
    sun = arcade.create_ellipse(1400, 1200, 150, 150, arcade.color.YELLOW)
    cloudp1 = arcade.create_ellipse(200, 1157, 65, 65, arcade.color.WHITE_SMOKE)
    cloudp2 = arcade.create_ellipse(240, 1157, 65, 65, arcade.color.WHITE_SMOKE)
    cloudp3 = arcade.create_ellipse(280, 1157, 65, 65, arcade.color.WHITE_SMOKE)
    cloud2p1 = arcade.create_ellipse(400, 1148, 70, 70, arcade.color.WHITE_SMOKE)
    cloud2p2 = arcade.create_ellipse(490, 1150, 70, 70, arcade.color.WHITE_SMOKE)
    cloud2p3 = arcade.create_ellipse(445, 1150, 70, 70, arcade.color.WHITE_SMOKE)
    cloud3p1 = arcade.create_ellipse(570, 1157, 30, 30, arcade.color.WHITE_SMOKE)
    cloud3p2 = arcade.create_ellipse(590, 1157, 30, 30, arcade.color.WHITE_SMOKE)
    cloud3p3 = arcade.create_ellipse(610, 1157, 30, 30, arcade.color.WHITE_SMOKE)
    cloud4p1 = arcade.create_ellipse(700, 1150, 55, 55, arcade.color.WHITE_SMOKE)
    cloud4p2 = arcade.create_ellipse(740, 1150, 55, 55, arcade.color.WHITE_SMOKE)
    cloud4p3 = arcade.create_ellipse(780, 1150, 55, 55, arcade.color.WHITE_SMOKE)

    #=#=#=#=# Car Parts to create the car #=#=#=#=#
    car1p1 = arcade.create_rectangle(200, 900, 350, 75, arcade.color.RED)
    wheel1p1 = arcade.create_ellipse(80, 872, 70, 70, arcade.color.BLACK)
    wheel1p2 = arcade.create_ellipse(80, 872, 40, 40, arcade.color.GRAY)
    wheel1p3 = arcade.create_ellipse(80, 872, 20, 20, arcade.color.COOL_BLACK)
    wheel1p4 = arcade.create_ellipse(80, 880, 69, 69, arcade.color.ASH_GREY)

    wheel2p1 = arcade.create_ellipse(300, 872, 70, 70, arcade.color.BLACK)
    wheel2p2 = arcade.create_ellipse(300, 872, 40, 40, arcade.color.GRAY)
    wheel2p3 = arcade.create_ellipse(300, 872, 20, 20, arcade.color.COOL_BLACK)
    wheel2p4 = arcade.create_ellipse(300, 880, 69, 69, arcade.color.ASH_GREY)

    window1 = arcade.create_polygon([(150, 937), (200,980), (260, 937)], arcade.color.BABY_BLUE_EYES)
    window2 = arcade.create_polygon([(200, 937), (200, 980), (50, 937)], arcade.color.BABY_BLUE_EYES)
    front_bumper = arcade.create_polygon([(500, 937), (375, 863), (300, 937)], arcade.color.GRAY)
    spoiler = arcade.create_polygon([(25, 937), (22, 970), (35, 937)], arcade.color.RED)
    rocket = arcade.create_rectangle(13, 900, 25, 30, arcade.color.ORANGE_RED)

    car2p1 = arcade.create_rectangle(500, 630, 400, 65, arcade.color.PURPLE_NAVY)
    car2p2 = arcade.create_rectangle(490, 650, 500, 50, arcade.color.PURPLE_NAVY)
    exhaust =arcade.create_rectangle(265, 610, 120, 10, arcade.color.ASH_GREY)
    window3p1 = arcade.create_polygon([(325, 675), (410, 740), (420, 675)], arcade.color.BABY_BLUE_EYES)
    window3p2 = arcade.create_polygon([(410, 740), (420, 675), (610, 675)], arcade.color.BABY_BLUE_EYES)
    window3p3 = arcade.create_polygon([(550, 740), (410, 740), (610, 675)], arcade.color.BABY_BLUE_EYES)

    wheel3p1 = arcade.create_ellipse(375, 600, 69, 69, arcade.color.BLACK)
    wheel3p2 = arcade.create_ellipse(375, 608, 75, 75, arcade.color.ASH_GREY)
    wheel3p3 = arcade.create_ellipse(375, 600, 40, 40, arcade.color.GRAY)
    wheel3p4 = arcade.create_ellipse(375, 600, 20, 20, arcade.color.PURPLE_NAVY)

    wheel4p1 = arcade.create_ellipse(650, 600, 69, 69, arcade.color.BLACK)
    wheel4p2 = arcade.create_ellipse(650, 608, 75, 75, arcade.color.ASH_GREY)
    wheel4p3 = arcade.create_ellipse(650, 600, 40, 40, arcade.color.GRAY)
    wheel4p4 = arcade.create_ellipse(650, 600, 20, 20, arcade.color.PURPLE_NAVY)

    butterflyp2 = arcade.create_rectangle(875, 1000, 65, 8, arcade.color.BARBIE_PINK)
    butterflyp1 = arcade.create_ellipse(865, 1012, 30, 30, arcade.color.PURPLE_NAVY)
    butterflyp3 = arcade.create_ellipse(889, 1012, 30, 30, arcade.color.PURPLE_NAVY)
    butterflyp4 = arcade.create_ellipse(865, 985, 30, 30, arcade.color.PURPLE_NAVY)
    butterflyp5 = arcade.create_ellipse(889, 985, 30, 30, arcade.color.PURPLE_NAVY)


    #=#=#=#=# Start the render/draw #=#=#=#=#
    arcade.start_render()
    road.draw()
    flp1.draw()
    flp2.draw()
    flp3.draw()
    flp4.draw()
    flp5.draw()
    flp6.draw()

    road_divider.draw()
    road_divider2.draw()
    road_divider3.draw()
    sky.draw()
    sun.draw()
    cloudp1.draw()
    cloudp2.draw()
    cloudp3.draw()
    cloud2p1.draw()
    cloud2p2.draw()
    cloud2p3.draw()
    cloud3p1.draw()
    cloud3p2.draw()
    cloud3p3.draw()
    cloud4p1.draw()
    cloud4p2.draw()
    cloud4p3.draw()
    car1p1.draw()
    car2p1.draw()

    car2p2.draw()
    exhaust.draw()
    window3p1.draw()
    window3p3.draw()
    window3p2.draw()



    wheel1p4.draw()
    wheel1p1.draw()
    wheel1p2.draw()
    wheel1p3.draw()

    wheel2p4.draw()
    wheel2p1.draw()
    wheel2p2.draw()
    wheel2p3.draw()

    wheel3p2.draw()
    wheel3p1.draw()
    wheel3p3.draw()
    wheel3p4.draw()
    wheel4p2.draw()
    wheel4p1.draw()
    wheel4p3.draw()
    wheel4p4.draw()

    window2.draw()
    window1.draw()

    front_bumper.draw()
    spoiler.draw()
    extra_grass.draw()
    arcade.draw_text("Finish Line", 1270, 1015, arcade.color.BLACK)
    arcade.draw_text("Butterfly Lily (Friend)", 925, 1005)
    rocket.draw()

    butterflyp4.draw()
    butterflyp5.draw()
    butterflyp1.draw()
    butterflyp3.draw()
    butterflyp2.draw()




    arcade.finish_render()
    arcade.run()
main()