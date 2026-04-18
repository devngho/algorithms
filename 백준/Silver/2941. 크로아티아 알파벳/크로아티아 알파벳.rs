use std::io;

fn main() {
    let mut buf = String::new();
    let mut count = 0;
    io::stdin().read_line(&mut buf).unwrap();
    let buf = buf.trim_end().chars().collect::<Vec<_>>();
    for i in 0..buf.iter().count(){
        let first = buf[i];
        if i != buf.len()-1{
            let second = buf[i+1];
            match first{
                'c' => {
                    if second != '=' && second != '-'{
                        count += 1
                    }
                },
                'd' => {
                    if second == 'z'{
                        //dz
                        if i != buf.len()-2{
                            //dz??
                            if buf[i+2] != '='{
                                count += 1
                            }
                        }else{
                            count += 1
                        }
                    }else if second != '-'{
                        count += 1
                    }
                },
                'l' | 'n' => {
                    if second != 'j'{
                        count += 1
                    }
                }
                's' | 'z' => {
                    if second != '='{
                        count += 1
                    }
                },
                _ => count += 1
            }
        }else{
            count += 1;
        }
    }
    println!("{}", count);
}