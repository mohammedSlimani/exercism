pub fn is_leap_year(year: u64) -> bool {
    // every if statement needs an else or it will evaluate to ()
    //this code could use some cleaning up!
    if year % 4 == 0 {
        if year % 100 == 0 {
            if year % 400 == 0 {
                true
            } else {
                false
            }
        } else {
            true
        }
    } else {
        false
    }
}
