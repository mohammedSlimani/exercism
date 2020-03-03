pub fn nth(n: u32) -> u32 {
    let mut prime_counter = 0;
    let mut current_number = 2;
    loop {
        if is_prime(current_number) {
            prime_counter +=1;
            if prime_counter - 1 == n {
                return current_number;
            }
        }
        current_number +=1;
    }
}

fn is_prime(n: u32) -> bool {
    if n == 0 || n == 1{
        return false;
    }
    if n == 2 {
        return true;
    } 
    for nbr in 2..n-1 {
        if n%nbr == 0 {
            return false;
        }
    }
    return true;
}