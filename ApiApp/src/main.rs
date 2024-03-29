use rocket::{Request, Response};
use rocket::http::{ContentType, Status};
use rocket::response::content;

// Définition d'une structure pour stocker les routes
struct Routes;

impl Routes {
    // Fonction pour gérer la route "/"
    fn index(_req: &Request) -> content::Html<String> {
        content::Html(String::from("Navigate to http://localhost:8000/check/<type your Coin> to check details about this crypto!"))
    }

    // Fonction pour gérer la route "/check/<coin>"
    fn check(req: &Request) -> Response<'static> {
        let coin = req.get_param::<String>(0);
        
        match coin {
            Some(coin) => {
                let request_url = format!("https://api.coingecko.com/api/v3/coins/{}", coin);
                println!("{}", request_url);
                let resp = reqwest::blocking::get(&request_url).unwrap();

                if resp.status().is_success() {
                    let body = resp.text().unwrap();
                    Response::build()
                        .header(ContentType::Plain)
                        .sized_body(body.len(), std::io::Cursor::new(body))
                        .finalize()
                } else {
                    let response = format!("{} is not a coin!", coin);
                    Response::build()
                        .header(ContentType::Plain)
                        .sized_body(response.len(), std::io::Cursor::new(response))
                        .status(Status::BadRequest)
                        .finalize()
                }
            }
            None => Response::build()
                        .status(Status::BadRequest)
                        .finalize(),
        }
    }
}

// Fonction principale pour monter les routes et lancer l'application Rocket
fn main() {
    rocket::ignite()
        .mount("/", routes![
            Routes::index,
            Routes::check
        ])
        .launch();
}