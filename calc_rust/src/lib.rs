use pyo3::prelude::*;

#[pyfunction]
fn calculate_move(given: Board, player_side: CellStatus) -> PyResult<()> {
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn calc_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_move, m)?)?;
    Ok(())
}