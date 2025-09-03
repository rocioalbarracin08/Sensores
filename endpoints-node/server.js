import express from "express"

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

//Inicializar el servidor
app.listen(PORT, ()=>{
    console.log(`servidor corriendo en el puerto ${PORT}`);
}) //listen, para que el puerto este abierto
