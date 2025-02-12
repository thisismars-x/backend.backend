use gotham::state::State;

pub fn say_hello(state: State) -> (State, &'static str) {
    (state, "Hello, World")
}

pub fn main() {
    let addr = "127.0.0.1:5001";
    gotham::start(addr, || Ok(say_hello));
}
