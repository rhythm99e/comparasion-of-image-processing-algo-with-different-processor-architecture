import math
def estimate_performance(processor,algorithm_profile):
    totlapx=algorithm_profile['output_pixels']
    total_ops=algorithm_profile['total_ops']
    kernel=algorithm_profile['kernel']
    simd_width=processor.simd_width
    ops_per_second = processor.clock_speed* 1e9 * processor.ipc*simd_width#this is not very accurate 
    compute_time = total_ops / ops_per_second
    bytes_per_pixel = (algorithm_profile['data_read_per_pixel'] + algorithm_profile['data_write_per_pixel'])
    total_bytes = bytes_per_pixel * totlapx
    memory_time = total_bytes / (processor.memory_bandwidth* 1e9)
    execution_time = max(compute_time, memory_time)
    bottleneck = 'compute' if compute_time > memory_time else 'memory'
    return {
        "processor": processor.name,
        'execution_time': execution_time*1000,
        'compute_time': compute_time*1000,
        'memory_time': memory_time*1000,#convert to milliseconds
        'bottleneck': bottleneck,
    }
