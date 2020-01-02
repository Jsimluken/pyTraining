const tf = require("@tensorflow/tfjs")

class HyperScale extends tf.layers.Layer{
    constructor(config){
        super(config);
        this.value = config["value"]
    }

    computeOutputShape(inputShape) {
        return [inputShape[0], inputShape[1], inputShape[2], inputShape[3]]
      }

      call(inputs, kwargs) {
        let input = inputs;
        if (Array.isArray(input)) {
          input = input[0];
        }
        this.invokeCallHook(inputs, kwargs);
        var res = tf.mul(input,tf.scalar(this.value))
        
        //res.print()
        return res
      }

      static get className() {
        return 'HyperScale';
      }
      
      getConfig(){
        const config = {
          value:this.value
        }
        const baseConfig = super.getConfig();
        Object.assign(config, baseConfig);
        return config;
      }

}
tf.serialization.registerClass(HyperScale); 


var loadModel = async ()=>{
    var model = await tf.loadLayersModel("http://127.0.0.1:61712/web_model2/model.json")
    model.summary()
    return model
}

loadModel().then(
    model=>{
        model.predict(tf.ones([1,160,160,3])).print()
    }
)