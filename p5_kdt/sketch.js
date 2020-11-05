count = 0;

function setup()
{
	var width = 750;
	var height = 500;

	createCanvas(width, height);
	background(0);  
	for(var x=0; x<width; x+=width/10){
		for(var y=0;y<height;y+=height/5){

			stroke(125,125,125);
			strokeWeight(1);
			line(x,0,x,height);
			line(0,y, width, y);
		}
	}
	
	

	var data = [];
	for(let i=0;i<12;i++){
		var x=Math.floor(Math.random()*height);
		var y=Math.floor(Math.random()*height);
		data.push([x,y]);
		let c = color(255, 255, 255); 
		fill(c);
		circle(x, height-y, 7);
		textSize(12);
		text(x + ',' + y, x+5, height -y);
	}

	
	var root=build_kdtree(data);
	console.log(root)
	generate_dot(root);
	

}
