import matplotlib.pyplot as plt
import numpy as np
def plot_performance(results, output_file='results/performance.png'):
    #extract processor
    processors=[r['processor'] for r in results ]
    compute_times=[r['compute_time'] for r in results]
    memory_times=[r['memory_time'] for r in results]
    plt.figure(figsize=(10,6))#making the canvas large
    plt.barh(processors,compute_times,label="compute_time",color='blue')
    plt.barh(processors, memory_times, left=compute_times, color='coral', label='Memory Time')
    plt.xlabel('execution time')
    plt.ylabel('Processors')
    plt.title('Performance Comparison', fontsize=14)
    plt.legend(loc='lower right')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()
    print(f"Saved: {output_file}")
