import express from 'express'
import TPLSmartDevice from 'tplink-lightbulb'

const app = express()
const port = 3000
app.get('/', (req, res) => {
 
  let { command, hue, saturation } = req.query
  command = (command === '1')

  const light = new TPLSmartDevice('192.168.1.121')
  light.power(command, 0, {"hue":parseInt(hue),"saturation":parseInt(saturation),"color_temp":0,"brightness":40})
    .then(status => {
      res.send(status)
    })
    .catch(err => res.send(err))

})

app.listen(port, () => console.log(`Listening on port ${port}!`))