
var k=2


class Node{
	constructor(point, axis){
		this.point = point;
		this.left = null;
		this.right = null;
		this.axis = axis;
	}
}


function build_kdtree(points, depth=0){

		var axis = depth%k;

		if(points.length<=0)
			return null;

		if(points.length==1)
		{
			return new Node(points[0],axis);
		}	

		//console.log(axis,points)
		const sortAsc = (a, b) => a[axis] - b[axis];
		points.sort(sortAsc);
	
		var middle;
		middle = Math.floor(points.length/2)

		var l = points.slice(0,middle)
		var r = points.slice(middle+1)
		
		var node = new Node(points[middle].slice(0,k),depth+1);
		node.left = build_kdtree(l, depth+1);
		node.rigth = build_kdtree(r,depth+1);

		return node;
			
}

function getHeight(node)
{
	if(!node)
		return 0

	return getHeight(node.left)+getHeight(node.right)+1;
}


function print_nodes(temp, node, side)
{
	if(temp)
	{
		console.log("\""+node.point[0].toString()+","+node.point[1].toString() +"\"->\""+temp.point[0].toString()+","+ temp.point[1].toString()+"\"")
		// text.WriteLine("\""+node.point[0].toString()+","+node.point[1].toString() +"\"->\""+temp.point[0].toString()+","+ temp.point[1].toString()+"\"")

		print_nodes(temp.left, temp)
		print_nodes(temp.rigth, temp)
	}
}


function generate_dot(node)
{
	console.log("Digraph G {")
	// text.WriteLine("Digraph G {")
	if(node)
	{	
		print_nodes(node.left,node,text);
		print_nodes(node.rigth,node,text);
	}
	console.log("}");
	// text.WriteLine("}");

}

