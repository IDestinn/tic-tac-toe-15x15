use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn calculate_best_move(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_best_move, m)?)?;
    Ok(())
}