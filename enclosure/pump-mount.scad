// Droplet pump mount - printable in PETG
$fn = 48;

mount_width = 62;
mount_depth = 44;
mount_height = 18;

difference() {
    cube([mount_width, mount_depth, mount_height], center = true);
    translate([0, 0, 4])
        cylinder(h = mount_height, d = 30, center = true);
    translate([0, 0, -2])
        cylinder(h = 10, d = 8, center = true);
}

for (x = [-24, 24]) {
    translate([x, 16, 0])
        cylinder(h = mount_height, d = 4.2, center = true);
}
