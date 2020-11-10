
var k=2
var kn=5

class Node{
	constructor(point, axis){
		this.point = point;
		this.left = null;
		this.right = null;
		this.axis = axis;
	}
}

function distanceSquared(point1, point2){
	var distance = 0;
	for (var i = 0 ; i<k; i++)
		distance +=Math.pow((point1[i]-point2[i]),2);

	return Math.sqrt(distance);

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

function closest_point_brute_force(points, point){
	dist_less = 100000;

	for(var i of points)
	{
		dist = distanceSquared(i, point)
		console.log(i,dist)

		if(dist<dist_less)
		{
			dist_less = dist;
			pointless = i;
		}

	}
	console.log(dist_less);
	return pointless;
}


function naive_closest_point(node, point, depth = 0, best = null){

	if(node == null)
		return best;

	if(best == null || distanceSquared(node.point, point)<distanceSquared(best, point))
		best = node.point;
		
	if(point[depth % k]< node.point[depth % k])
		return naive_closest_point(node.left, point, depth +1 , best)
		
	else
		return naive_closest_point(node.rigth, point, depth +1 , best)  

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


function cercano(point, p1, p2)
{	
	if(!p1)
		return p2;

	if(!p2)
		return p1;

	if(distanceSquared(point, p1)<distanceSquared(point, p2))
		return p1; 

	else
		return p2;
}
	

function closest_point(node, point, depth = 0, best=null){

	if(node == null)
		return null;

	var next_branch = null;
	var opposite_branch = null;

	if(point[depth%k] < node.point[depth%k]){
		next_branch = node.left;
		opposite_branch = node.rigth;

	}else{
		next_branch = node.rigth;
		opposite_branch = node.left;
	}


	best = cercano(point, closest_point(next_branch, point, depth+1), node.point);

	if(distanceSquared(point, best) > Math.abs(point[depth%k] - node.point[depth%k]))
	{
		best = cercano(point, closest_point(opposite_branch, point, depth+1), node.point);
	}

	return best;
	
}

//FInal
function KNN(node, point, kpoints ,depth = 0){
	count++;
	if(node==null)
		return null;

	var next_branch;
	var opposite_branch;
	var temp;
		
	if(point[depth % k]< node.point[depth % k])
	{	next_branch = node.left;
		opposite_branch = node.rigth;
	}
		
	else		
	{
		next_branch = node.rigth;
		opposite_branch = node.left;	
	}


	cercano(point, KNN(next_branch, point, kpoints, depth +1), node.point);
	//count++;

	if(kpoints.length<kn)
	{
		temp = node.point;
		temp.push(distanceSquared(point,temp));
		kpoints.push(temp);

		const sortDist = (a, b) => a[2] - b[2];
		kpoints.sort(sortDist);
	}

	else
	{	
		temp = node.point;
		temp.push(distanceSquared(point,temp));
		if(temp[2]<kpoints[kpoints.length-1][2])
		{
			kpoints.pop();
			kpoints.push(temp);
			const sortDist = (a, b) => a[2] - b[2];
			kpoints.sort(sortDist);

		}
		
	}
	

	if(kpoints.length<kn || kpoints[0][2]>=Math.abs(point[depth%k]-node.point[depth%k]))
	{
		cercano(point, KNN(opposite_branch, point, kpoints, depth +1), node.point);

	}
	
}
