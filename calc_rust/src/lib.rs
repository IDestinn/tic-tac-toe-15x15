use pyo3::prelude::*;

#[pyclass]
struct Board {}

#[pyclass]
enum CellStatus {}

#[pyfunction]
fn calculate_move(given: Board, player_side: CellStatus) -> PyResult<()> {
    let mut depth = given.get_valid_moves()
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn calc_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Board>()?;
    m.add("CellStatus", pyo3::types::PyType::new::<CellStatus>())?;
    m.add_function(wrap_pyfunction!(calculate_move, m)?)?;
    Ok(())
}