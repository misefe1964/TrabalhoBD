--Consulta 1:
select s.idSetor, avg(Salario) 
from Colaborador as c 
inner join Setor as s 
on c.idSetor = s.idSetor
group by s.idSetor;

--Consulta 2:
select c.idColaborador, count(pw.idProjeto) 
from Colaborador as c 
inner join Desenvolve as d 
on c.idColaborador = d.idColaborador
inner join ProjetoWeb as pw 
on d.idProjeto = pw.idProjeto
group by c.idColaborador;
--Consulta 3:
Select c.idCliente, sum(Valor) 
from Cliente as c inner join Pedido as p 
on c.idCliente = p.idCliente
inner join Gera as g 
on p.idPedido = g.idPedido
inner join OrdemdeServico as os 
on g.idOrdem = os.idOrdem
group by c.idCliente;