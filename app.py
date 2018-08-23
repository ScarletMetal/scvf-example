from scvf import cv_loop
from scvf.io import NetworkTableIO

from pipelines.reflectives_pipeline import GripPipeline as ReflectivePipeline

nt_io = NetworkTableIO("127.0.0.1", "ImageProcessing")

pipelines = {"reflective": ReflectivePipeline()}

cv_loop.start(pipelines, output_consumer=nt_io.output_consumer, settings_supplier=nt_io.settings_supplier)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    cv_loop.end()