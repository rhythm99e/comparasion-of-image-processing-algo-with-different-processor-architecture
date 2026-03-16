import os
import cv2
from processor import processor_o
from algorith import ALGORITHMS
from performance import estimate_performance
from visualization import plot_performance
def main():
    os.makedirs("results",exist_ok=True)
    image_path="../image/base.jpg"
    if not os.path.exists(image_path):
        print(f"Image not found at {image_path}")
        return
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    algorithm = ALGORITHMS['sobel']
    profile = algorithm.profile(image)
    print(f"{'='*70}")
    print(f"ALGORITHM: {algorithm.name}")
    print(f"{'='*70}\n")
    processors = list(processor_o.values())
    print(f"{'='*70}")
    print(f"PERFORMANCE ESTIMATES")
    print(f"{'='*70}\n")
    
    results = []
    for proc in processors:
        perf=estimate_performance(proc,profile)#profile gives the info about the algo and image, proc give about the processor
        print(f"Processor: {proc.name}")
        print(f"compute time:{perf['compute_time']:.6f} seconds")
        print(f"memory time:{perf['memory_time']:.6f} seconds")
        print(f"bottleneck: {perf['bottleneck']}")
        print(f"{'-'*40}\n")
        results.append(perf)
        print(f"{'='*70}")
    print(f"GENERATING VISUALIZATIONS")
    print(f"{'='*70}\n")
    
    plot_performance(results, 'results/performance.png')
    
if __name__ == '__main__':
     main()


