var fs = require("fs");

function read_file(filepath) {
    let text = fs.readFileSync(filepath)
        .toString()
        .trim()
        .split("\n")

    return text;
}

//----------------------part1-----------------------
// funktion gibt die richtung nach einer drehung zurück
function change_direction(previous_direction, input) {
    var direction_dict = {
        "E" : [0],
        "N" : [270, -90],
        "W" : [180, -180],
        "S" : [90, -270]
    }
    if (input.substring(0,1) == "R") { // nur der nullte bis (exklusive) dem ersten
        var direction = direction_dict[previous_direction][0];
        direction += parseInt(input.substring(1)); // alle ausser der erste im string
        var modulo = direction % 360;
        for (var key in direction_dict) {
            if (direction_dict[key].includes(modulo) === true) {
                return key
            }
        }

    }
    else if (input.substring(0,1) == "L") {
        var direction = direction_dict[previous_direction][0];
        direction -= parseInt(input.substring(1));
        var modulo = direction % 360;
        for (var key in direction_dict) {
            if (direction_dict[key].includes(modulo) === true) {
                return key
            }
        }
    }
}

function manhattan_dist(data) {
    var direction = "E";
    var x_position = 0;
    var y_position = 0;
    for (x in data) {
        if (data[x].substring(0,1) == "N") { // das boot fährt seitwärts usw.
            y_position += parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "S") {
            y_position -= parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "E") {
            x_position += parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "W") {
            x_position -= parseInt(data[x].substring(1));
        }
        else if (data[x].substring(0,1) == "R" || data[x].substring(0,1) == "L") { // das boot wechselt seine richtung
            direction = change_direction(direction, data[x]);
            console.log(direction);
        }
        else if (data[x].substring(0,1) == "F") { // das boot fährt geradeaus
            if (direction == "E") {
                x_position += parseInt(data[x].substring(1));
            }
            else if (direction == "W") {
                x_position -= parseInt(data[x].substring(1));
            }
            else if (direction == "N") {
                y_position += parseInt(data[x].substring(1));
            }
            else if (direction == "S") {
                y_position -= parseInt(data[x].substring(1));
            }
        }
    }
    return Math.abs(x_position) + Math.abs(y_position);
}

function main() {
    var data = read_file("test_12.txt");
//----------------------part1-----------------------
    console.log(manhattan_dist(data));
}

main();