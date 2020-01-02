docker run -it --rm -v `pwd`:/opt/model \
    jsimluken/tfjs tensorflowjs_converter \
    --input_format=keras \
    --output_format=tfjs_layers_model \
    /opt/model/hyper.h5\
    /opt/model/web_model2