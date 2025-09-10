import mysql from "mysql2/promise"//Va poder recibir promesas: PARA
import dotenv from "dotenv";

dotenv.config();

//consfiguración de la conexión
const pool = mysql.createPool (
    {
        host: process.env.DB_HOST, //Poceso de ejecucion y en ese proceso va y busca las variables de | Sacamos el valor del archivo con variables de entorno
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        
        //Cosas de configuracion | Lo de arriba son datos necesarios
        waitForConnections: true,
        connectionLimit: 10,
        queueLimit: 0
    }
)

export default pool;