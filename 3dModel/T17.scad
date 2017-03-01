/*
 * Main Frame
 */
difference(){
    cube(150);//Main thing
    translate([10,25,20]){cube([130,100,150]);}//The cube that empties the major thing
    translate([0,25/2-5,80]){cube([150,10,150-70]);}//
    translate([0,150-25/2-5,80]){cube([150,10,150-70]);}
    translate([0,70,70])cube([75,10,200]);
    translate([0,50,20])cube([25,50,25]);
    translate([47.5*3,0,0]){
        rotate([0,0,90]){
            translate([0,50,35+15])cube([30,55,30]);
        }
    }
    translate([42,0,20])cube([46,40,19]);
    translate([47.5*3,125,0]){
        rotate([0,0,90]){
            translate([0,50,35+15])cube([30,55,30]);
        }
    }
    translate([42,125,20])cube([46,40,19]);
    for(y=[5:20:145]){translate([y,150,145])rotate([90,0,0])cylinder($fn=25,d=5,150);}
    for(y=[5:20:145]){translate([y,150,137])rotate([90,0,0])cylinder($fn = 25, d=5,150);}
    translate([20,10,100]){
    rotate([90,0,0]){
            linear_extrude(15){
                text("\u03BA\u03B1\u03BA\u03CC\u03C2 m\u0119\u017Cczyzna");
            }
        }
    }
    translate([130,140,100]){
    rotate([90,00,180]){
            linear_extrude(17){
                text("\u03BA\u03B1\u03BA\u03CC\u03C2 m\u0119\u017Cczyzna");
            }
        }
    }
    translate([145,22.5,100]){
    rotate([90,0,90]){
            linear_extrude(15){
                text("\u03BA\u03B1\u03BA\u03CC\u03C2 m\u0119\u017Cczyzna");
            }
        }
    }
}
difference(){
    translate([0,50,20])cube([30,55,30]);
    translate([0,52.5,22.5])cube([30,50,25]);
}
translate([47.5*3,0,0]){
    rotate([0,0,90]){
        difference(){
            translate([0,50,35+15])cube([30,55,30]);
            translate([0,52.5,35+2.5+15])cube([30,50,25]);
        }
    }
}
translate([-11,150,0]){
    rotate([0,0,-90]){
        difference(){
            translate([0,50,35+15])cube([30,55,30]);
            translate([0,52.5,35+2.5+15])cube([30,50,25]);
        }
    }
}
//Batteries
difference(){
    translate([105,25,20])cube([35,100,100]);
    translate([110,27,20])cube([25,45,100]);
    translate([110,77,20])cube([25,45,100]);
}
translate([10,25,0])cube([10,10,120]);
translate([10,115,0])cube([10,10,120]);