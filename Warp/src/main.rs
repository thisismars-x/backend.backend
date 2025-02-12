use warp::Filter;

#[tokio::main]
async fn main() {
    let hello = warp::path!().map(|| "Hello, World");

    warp::serve(hello).run(([127, 0, 0, 1], 3003)).await;
}
