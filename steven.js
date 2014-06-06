
//FightCode can only understand your robot
//if its class is called Robot
var Robot = function(robot) {

};

Robot.prototype.onIdle = function(ev) {
    var robot = ev.robot;
		robot.ahead(50);
  	robot.turnLeft(100);
  	robot.rotateCannon(25);
  	robot.ahead(50);
		robot.turnRight(10);
  	robot.rotateCannon(-25);
};

Robot.prototype.onWallCollision = function(ev) { 
		var robot = ev.robot;
  	robot.back(50);
  	robot.turnRight(1180);
};

Robot.prototype.onScannedRobot = function(ev) {
    var robot = ev.robot;
    robot.fire();
    robot.ahead(50);

};

Robot.prototype.onRobotCollision = function(ev) {
  	var robot = ev.robot;
  	robot.back(35);
  	robot.turn(20);
  	robot.back(30);
  
};

Robot.prototype.onHitByBullet = function(ev){
		var robot = ev.robot
    robot.back(20);
  	robot.turn(-20);
  	robot.ahead(30);
};