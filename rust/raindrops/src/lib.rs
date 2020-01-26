pub fn raindrops(n: u32) -> String {
    let mut rain_sound = String::from("");
    let mut changed = false;

    if n%3 == 0 {
        rain_sound.push_str("Pling");
        changed = true;
    }
    if n%5 == 0 {
        rain_sound.push_str("Plang");
        changed = true;
    }
    if n%7 == 0 {
        rain_sound.push_str("Plong");
        changed = true;
    }

    if !changed {
        n.to_string()
    } else{
        rain_sound
    }

}
