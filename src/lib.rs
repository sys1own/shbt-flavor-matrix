
use pyo3::prelude::*;

#[pyfunction]
fn get_geometric_kappa() -> PyResult<String> {
    Ok("0.16180339887498948482".to_string())
}

#[pymodule]
fn anyon_simulator(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("PARENT", "K-742")?;
    m.add_function(wrap_pyfunction!(get_geometric_kappa, m)?)?;
    Ok(())
}
