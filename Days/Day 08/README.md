# + [Taller de Rust Language](https://www.youtube.com/watch?v=2YWAIQQ8AA4)
## Por que Rust?
- Rust is a systems programming language. 
- Safety, speed, and concurrency.
- Zero cost abstractions.
- Empowering everyone to build reliable and efficient software.

    - Performance & control 
    - Reliability & safety
    - Productivity 

## Instalación
- [Instalación](https://www.rust-lang.org/tools/install)

## Cargo 
- Cargo es el gestor de paquetes de Rust.

`cargo new hello_world`

`cargo build --release`

`cargo run`

`cargo test`

`cargo fmt`

`cargo check`

`cargo doc --open`

## Sintaxis

#### Variables
- let (por derfecto inmutable)
- mutable mut 
- binding 
- shadow
- inferencia de tipos
#### Tipos de datos
- Numericos 
    - i8, i16, i32, i64
    - u8, u16, u32, u64
    - unsize, isize
- Bool
- Char
- Compuetos
    - Tuplas
    - Arrays
- Colecciones
    - Vector
    - String
    - HashMap

#### Funciones
```rust
    fn add_uno(a: i32) -> i32{
        a + 1
    }
```
#### Structs
```rust
    struct Point {
        x: i32,
        y: i32,
    }
```
#### Enums
```rust
    enum Color {
        Red,
        Green,
        Blue,
    }
```
#### Options 
```rust
    enum Option<T> {
        Some(T),
        None,
    }

    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
```

#### Control de flujo
- if
- loop
- while
- for
- match
- if let

#### impl 
```rust
    struct Rectangle {
        width: u32,
        height: u32,
    }

    impl Rectangle {
        fn area(&self) -> u32 {
            self.width * self.height
        }
    }
    // Associated functions
    impl Rectangle {
        fn square(size: u32) -> Rectangle {
            Rectangle { width: size, height: size }
        }
    }

    let sq = Rectangle::square(3);
```

## Creates
- Paquete 
- Create 
- Modulo 

## Ownership & Borrowing
- Reglas Ownership
    - Cada valor en Rust tiene una variable que es su propietario.
    - Solo puede haber un propietario a la vez.
    - El propietario se libera cuando sale del alcance.
        - Move 
        - Copy

## References & Borrowing

```rust
    let s1 = String::from("hello");
    let len = &s1;
    println!("{}", s1);
```

#### Tipos de Referencias
- &T: Referencia a un valor inmutable.(shared)
- &mut T: Referencia a un valor mutable.(exclusive)

## Testing
- Funciones marcadas con #[test]
- Se utiliza macros para realizar las afirmaciones. (assert_eq!, assert_ne!, assert!)
- Otros atributus:
    - #[ignore]
    - #[should_panic]
    - should_panic(expected = "Mensaje de error")

#### Test Modules 
- Organizar los tests en modulos.
- #[cfg(test)]

#### Test Integration
- Se usa el directorio /tests (al mismo nivel que /src)
- Compila cada archivo como un crate separado y no necesita #[cfg(test)].
- Solo se puede testear library crate. 

#### Investigar
- Traits
- Traits bounds
- Generics
- lifetimes
- interiores mutability 
- concurrency


## Adopting Rust on your Team

- https://rocket.rs/
- https://actix.rs/

- Should your team adopt the Rust programming language? [Video](https://www.youtube.com/watch?v=Gnp4XP1b82E)

- How to introduce Rust to an existing project [Video](https://www.youtube.com/watch?v=l--5nx_q0_Y)
