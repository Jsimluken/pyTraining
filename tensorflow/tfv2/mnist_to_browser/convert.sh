#!/bin/bash
docker run -it --rm -v `pwd`/model:/opt/model \
    jsimluken/tfjs tensorflowjs_converter \
    --input_format=keras \
    --output_format=tfjs_graph_model \
    /opt/model/tiny_mnist.h5\
    /opt/model/web_model2