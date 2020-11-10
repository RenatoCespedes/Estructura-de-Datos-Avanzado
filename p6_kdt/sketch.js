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
	
	

	// var data = [];
	// for(let i=0;i<12;i++){
	// 	var x=Math.floor(Math.random()*height);
	// 	var y=Math.floor(Math.random()*height);
	// 	data.push([x,y]);
	// 	let c = color(255, 255, 255); 
	// 	fill(c);
	// 	circle(x, height-y, 7);
	// 	textSize(12);
	// 	text(x + ',' + y, x+5, height -y);
	// }
	//EJERCICIO 2
	// var data = [
	// [40, 70],
	// [70, 130],
	// [90, 40],
	// [110, 100],
	// [140, 110],
	// [160, 100],
	// [150, 30]
	// ];



	//EJERCICIO 3
	var data = [
	[40, 70],
	[70, 130],
	[90, 40],
	[110, 100],
	[140, 110],
	[160, 100],
	];
	


	
	for(let i=0;i<data.length;i++){
		
		let c = color(255, 255, 255); 
		fill(c);
		circle(data[i][0], height-data[i][1], 7);
		textSize(11);
		text(data[i][0] + ',' + data[i][1], data[i][0]+5, height -data[i][1]);
	}

	// var point = [140, 90];
	var point=[300,60]
	let col= color(255,19,0);
	fill(col);
	circle(point[0],height - point[1],11);

	var root=build_kdtree(data);
	console.log(root)
	generate_dot(root);

	// console.log(closest_point_brute_force(data, point));
	// console.log("\n");

	// console.log(naive_closest_point(root, point));
	// console.log("\n")

	// console.log(closest_point(root, point));
	
	KNNPoints=[]
	KNN(root, point, KNNPoints);
	console.log(KNNPoints)
	// console.log(count);
	for(let i=0;i<KNNPoints.length;i++){
		let c = color(0, 4, 255); 
		fill(c);
		circle(KNNPoints[i][0], height-KNNPoints[i][1], 7);
		textSize(11);
		text(KNNPoints[i][0] + ',' + KNNPoints[i][1], KNNPoints[i][0]+5, height -KNNPoints[i][1]);
	}
	
}
