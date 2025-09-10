import express from "express"
import pool from "./db.js" //Atenta con el ".js" que faltaba

const app = express();//
const PORT = 3000; //Constante REAL cuando el nombre va todo en mayus, antees creamos constantes nuevas a partir de contantes anteriores

app.use(express.json());

//APLICAMOS LA FUNCION FLECHA PARA QUE FUNCIONE: ("ruta",()=>{})
app.get('/',(req, res) => {
    res.send('este es un endpoint hecho con express'); //send: es como un return para que te lo devuelva en la consola
})

/*-----------------------------
ENDPOINT CON PARAMETRO (para crearlo necesitamos rutas)
-------------------------------*/
app.get('/api/user/:id', (req,res) =>{
    
    //destructuración: capturar un valor de un objeto
    //params responde al "de donde lo voy a sacar"
    const {id}= req.params;
    res.json({ message: `El usuario con id ${id} es pepito`}); //json or 
})

app.get('/api/search', (req, res) => {
    const {name, lastname} = req.query
    res.json({
        firstname: name,
        lastname,
    });
    //http://localhost:PUERTO/api/search?name=Federico&lastname=Villace
});

//Endpoint POST
app.post('/api/user',(req,res)=>{  
    const {name, email} = req.body
    res.json({message: 'Usuario creado', data: { name, email } })
})

//-------------------------------------------------
//Rutas usando el metodo put
app.put('/api/user/:id', (req, res) => {
    const {id} = req.params
    const {name,email} = req.body
    res.json({
        message: `Este es el usuario con id ${id}`,
        data: {name, email},
    })
})

//Rutas usando el método delete
app.delete('/api/user/:id', (req, res) => {
    const{id} = req.params //busca en 
    res.json({massage: `Usuario con id ${id} eliminado`})
})


//Endpoint DB con metodo GET
//asyn: nuestro código se va ejecutar de forma asíncrona (Peticion al servidor y hay que esperarla)
//await: Espera, siempre con algo asincrono lo usamos
app.get('/api/productos', async(req,res) => {
    
    //Código a probar
    try{
        const[rows] = await pool.query("SELECT * from productos")
        res.json(rows);
    }
    catch(error){
        console.log(error)
        res.status(500).json({error: "Error en la consulta"})
    }
})

//Inicializar el servidor: Va al final para que el código siga corriendo, si lo pongo antes evade los últimos endpoints
app.listen(PORT, ()=>{
    console.log(`servidor corriendo en el puerto ${PORT}`);
}) //listen, para que el puerto este abierto
