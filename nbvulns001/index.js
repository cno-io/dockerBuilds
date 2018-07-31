const fastify = require('fastify')
const args = require('yargs').argv
const request = require('request')
const fastifyStatic = require('fastify-static')
const {join} = require('path')
const url = require("url")

const validContentTypes = ['image/jpeg', 'image/jpg', 'image/png']

const defaultContentTypes = {png: 'image/png', jpg: 'image/jpeg'}

const PORT = 8080;
const HOST = '0.0.0.0';

const app = fastify()

app.get('/extimage', (req, reply) => {
  const path = req.query.p
  if (typeof path != 'string' || path.length < 1) return reply.code(400).send('Malformed Request')
  let target
  try {
    target = url.parse(path)
  } catch(err) {
    return reply.code(400).send('Malformed URL')
  }

  const {href, protocol} = target

  if (typeof protocol != 'string' || !['http:', 'https:'].includes(protocol)) return reply.code(400).send('Malformed Protocol')
  if (typeof href != 'string' || href.length < 1) return reply.code(400).send('Malformed URL')

  request(href, {encoding: null}, (err, response, body) => {
    if (err) {
      console.log(err)
      return reply.code(500).send('Internal Error')
    }

    let contentType
    let extension = href.split('.')
    extension = extension[extension.length - 1]

    if (validContentTypes.includes(response.headers["content-type"])) {
      contentType = response.headers["content-type"]
    } else if (defaultContentTypes.hasOwnProperty(extension)) {
      contentType = defaultContentTypes[extension]
    } else {
      contentType = defaultContentTypes.jpg
    }

    return reply.code(response.statusCode).type(contentType).header('cache-control', 'max-age='+ (60 * 60 * 24 * 5)).send(body)
  })
})

if ((args.s || args.static) === true) {
  console.log('Serving Static Content')
  app.register(fastifyStatic, {root: '/usr/src/app/static'})
}

app.listen(PORT, HOST, (err) => {
  if (err) return console.err(err)
  console.log('Server Listening on :'+PORT)
})
