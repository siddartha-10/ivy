from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_test


@handle_test(
    fn_tree="functional.ivy.experimental.triu_indices",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        num_arrays=3,
        min_value=0,
        max_value=10,
    ),
    test_with_out=st.just(False),
    test_gradients=st.just(False),
    test_instance_method=st.just(False),
)
def test_triu_indices(
    *,
    dtype_and_x,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x = dtype_and_x
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        test_flags=test_flags,
        fw=backend_fw,
        on_device=on_device,
        fn_name=fn_name,
        n_rows=int(x[0]),
        n_cols=int(x[1]),
        k=int(x[2]),
    )


# vorbis_window
@handle_test(
    fn_tree="functional.ivy.experimental.vorbis_window",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        min_value=1,
        max_value=10,
    ),
    dtype=helpers.get_dtypes("float", full=False),
    test_gradients=st.just(False),
    test_instance_method=st.just(False),
)
def test_vorbis_window(
    *,
    dtype_and_x,
    dtype,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x = dtype_and_x
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        test_flags=test_flags,
        atol_=1e-02,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        window_length=int(x[0]),
        dtype=dtype[0],
    )


# hann_window
@handle_test(
    fn_tree="functional.ivy.experimental.hann_window",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        min_value=1,
        max_value=10,
    ),
    periodic=st.booleans(),
    dtype=helpers.get_dtypes("float", full=False),
    test_gradients=st.just(False),
    test_instance_method=st.just(False),
)
def test_hann_window(
    *,
    dtype_and_x,
    periodic,
    dtype,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x = dtype_and_x
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        size=int(x[0]),
        periodic=periodic,
        dtype=dtype[0],
    )


# kaiser_window
@handle_test(
    fn_tree="functional.ivy.experimental.kaiser_window",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        min_value=1,
        max_value=10,
    ),
    periodic=st.booleans(),
    beta=st.floats(min_value=0, max_value=5),
    dtype=helpers.get_dtypes("float", full=False),
    test_gradients=st.just(False),
)
def test_kaiser_window(
    *,
    dtype_and_x,
    periodic,
    beta,
    dtype,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x = dtype_and_x
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        window_length=int(x[0]),
        periodic=periodic,
        beta=beta,
        dtype=dtype[0],
    )


# kaiser_bessel_derived_window
@handle_test(
    fn_tree="functional.ivy.experimental.kaiser_bessel_derived_window",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        min_value=1,
        max_value=10,
    ),
    periodic=st.booleans(),
    beta=st.floats(min_value=1, max_value=5),
    dtype=helpers.get_dtypes("float", full=False),
    test_gradients=st.just(False),
    test_instance_method=st.just(False),
)
def test_kaiser_bessel_derived_window(
    *,
    dtype_and_x,
    periodic,
    beta,
    dtype,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x = dtype_and_x
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        window_length=int(x[0]),
        periodic=periodic,
        beta=beta,
        dtype=dtype[0],
    )


# hamming_window
@handle_test(
    fn_tree="functional.ivy.experimental.hamming_window",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        min_value=1,
        max_value=10,
    ),
    periodic=st.booleans(),
    dtype_and_f=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float"),
        max_num_dims=0,
        num_arrays=2,
        min_value=0,
        max_value=5,
    ),
    dtype=helpers.get_dtypes("float", full=False),
    test_gradients=st.just(False),
    test_instance_method=st.just(False),
)
def test_hamming_window(
    *,
    dtype_and_x,
    periodic,
    dtype_and_f,
    dtype,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype1, x = dtype_and_x
    input_dtype2, f = dtype_and_f
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype1 + input_dtype2,
        test_flags=test_flags,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        window_length=int(x[0]),
        periodic=periodic,
        alpha=float(f[0]),
        beta=float(f[1]),
        dtype=dtype[0],
    )


@handle_test(
    fn_tree="functional.ivy.experimental.tril_indices",
    dtype_and_n=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("integer"),
        max_num_dims=0,
        num_arrays=2,
        min_value=0,
        max_value=10,
    ),
    k=helpers.ints(min_value=-11, max_value=11),
    test_with_out=st.just(False),
    test_gradients=st.just(False),
    test_instance_method=st.just(False),
)
def test_tril_indices(
    *,
    dtype_and_n,
    k,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x = dtype_and_n
    helpers.test_function(
        input_dtypes=input_dtype,
        ground_truth_backend=ground_truth_backend,
        test_flags=test_flags,
        fw=backend_fw,
        on_device=on_device,
        fn_name=fn_name,
        n_rows=int(x[0]),
        n_cols=int(x[1]),
        k=k,
    )


# eye_like
@handle_test(
    fn_tree="functional.ivy.experimental.eye_like",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_num_dims=1,
        max_num_dims=1,
        min_dim_size=1,
        max_dim_size=5,
    ),
    k=helpers.ints(min_value=-10, max_value=10),
    test_gradients=st.just(False),
    number_positional_args=st.just(1),
)
def test_eye_like(
    *,
    dtype_and_x,
    k,
    test_flags,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    dtype, x = dtype_and_x
    helpers.test_function(
        input_dtypes=dtype,
        test_flags=test_flags,
        on_device=on_device,
        fw=backend_fw,
        fn_name=fn_name,
        x=x[0],
        k=k,
        dtype=dtype[0],
        device=on_device,
        ground_truth_backend=ground_truth_backend,
    )


# stft
@st.composite
def valid_stft_params(draw):
    # draw data types
    dtype = draw(helpers.get_dtypes("numeric"))
    # Draw values for the input signal x
    x = draw(
        st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2, max_size=1000)
    )
    # Draw values for the window function size
    frame_length = draw(st.integers(min_value=2, max_value=1000))
    # Draw values for the hop size between adjacent frames
    frame_step = draw(st.integers(min_value=1, max_value=frame_length))
    # Draw values for the window function type
    window_fn = draw(
        st.sampled_from(["hann", "hamming", "rectangle", "blackman", "bartlett"])
    )
    # Draw values for the FFT size
    fft_length = draw(st.integers(min_value=frame_length, max_value=frame_length * 4))
    return dtype, x, frame_length, frame_step, window_fn, fft_length


@handle_test(
    fn_tree="functional.ivy.experimental.stft",
    dtype_x_and_args=valid_stft_params(),
    test_with_out=st.just(False),
)
def test_stft(
    *,
    dtype_x_and_args,
    frontend,
    test_flags,
    fn_tree,
    on_device,
):
    dtype, x, frame_length, frame_step, window_fn, fft_length = dtype_x_and_args
    helpers.test_frontend_function(
        input_dtypes=dtype,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        signals=x[0],
        frame_length=frame_length,
        frame_step=frame_step,
        window_fn=window_fn,
        fft_length=fft_length,
        pad_end=True,
        name=None,
    )
