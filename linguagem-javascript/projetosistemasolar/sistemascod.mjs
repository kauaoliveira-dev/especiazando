import { createServer } from 'http';
import { parse } from 'url';
import { readFile } from 'fs';

//Criação do servidor
const hostname = '127.0.0.1';
const port = 80;

createServer(
    function(req, res) {
        let k = parse(req.url, true);
        let filename = "./projetosistemasolar" + k.pathname;
        // A URL não pode ter caracteres especiais, senão o software não localiza
        console.log(k);
        console.log(filename);

        readFile(filename, function(err, data) {
            console.log(err);
            if (err) {
                res.writeHead(404, {'Content-Type': 'text/html'});
                return res.end("404 not Found");
            }
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
        });
    }
).listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});



