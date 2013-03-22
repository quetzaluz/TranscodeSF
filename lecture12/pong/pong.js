window.addEventListener("load", init, false);

// Global variables.
var objects = [];
var paddles = [];
var balls = [];
var player_paddle;
var computer_paddle;
var canvas;
var context;
var last_time;

// GameObject class.  GameObjects are rectangles (x, y, width, height).
function GameObject() {
    this.x = 0;
    this.y = 0;
    this.width = 0;
    this.height = 0;
    this.velocity_x = 0;
    this.velocity_y = 0;
    this.color = "black";
}

GameObject.prototype.draw = function(ctx) {
    // Draw a rectangle with an outline.
    ctx.lineWidth = 2;
    ctx.strokeStyle = 'black';
    ctx.strokeRect(this.x, this.y, this.width, this.height);
    ctx.fillStyle = this.color;
    ctx.fillRect(this.x, this.y, this.width, this.height);
}

PlayerScore.prototype = new GameObject();
PlayerScore.prototype.constructor = PlayerScore;
function PlayerScore() {
  	this.font = "20px Arial";
}

PlayerScore.prototype.draw = function(ctx) {
	ctx.fillText(canvas.width/2, canvas.height/2);
}

ComputerScore.prototype = new GameObject();
ComputerScore.prototype.constructor = ComputerScore;
function ComputerScore() {
  	this.font = "20px Arial";
}

ComputerScore.prototype.draw = function(ctx) {
	ctx.fillText(computer_score, 10, canvas.height - 10);
}



//
//
// GameObject.prototype.draw = function(p_score) {
//	this.font = "20px Arial";
//	this.fillText(player_score, 10, canvas.height - 10);
// }
//
// GameObject.prototype.draw = function(c_score)


// Define Ball class.  Javascript inheritance is kind of gross.
Ball.prototype = new GameObject();
Ball.prototype.constructor = Ball;
function Ball() {
    this.width = 10;
    this.height = 10;
    this.color = "green";

}

Ball.prototype.update = function(time_delta) {
    this.x += this.velocity_x * time_delta;
    this.y += this.velocity_y * time_delta;

    // Rebound if this ball hits the top or bottom edge.
    if (this.y < 0)
        this.velocity_y = Math.abs(this.velocity_y);
    if (this.y > canvas.height - this.height)
        this.velocity_y = -1 * Math.abs(this.velocity_y);
}

// Define Paddle class.
Paddle.prototype = new GameObject();
Paddle.prototype_constructor = Paddle;
function Paddle() {
    this.width = 5;
    this.height = 50;
    this.color = "blue";
    this.speed = 0.5;
    this.reflect_dir = 1;
}

Paddle.prototype.update = function(time_delta) {
    this.x += this.velocity_x * time_delta;
    this.y += this.velocity_y * time_delta;
	
    // FIXME: paddles shouldn't be able to go off the top or bottom.
	//
	if (this.y < 0)
		this.y = 0;
	if (this.y > canvas.height - this.height)
		this.y = canvas.height - this.height;
}

function animate() {
    window.requestAnimationFrame(animate);

    // Figure out how much time has passed since the last time animate was
    // called.
    var time_delta = 0;
    var this_time = new Date().getTime();
    if (last_time) {
        time_delta = this_time - last_time;
    }
    last_time = this_time;

    run_computer_ai();

    // Move all objects (paddles and balls).
    for (var x = 0; x < objects.length; x++) {
        objects[x].update(time_delta);
    }

    // Check all balls against all paddles to see if they hit each other.
    for (var b = 0; b < balls.length; b++) {
        for (var p = 0; p < paddles.length; p++) {
            // FIXME: maybe the ball should speed up if it collides?
            checkCollision(balls[b], paddles[p]);
        }
    }

    // Clear the background.
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Draw all objects.
    for (var x = 0; x < objects.length; x++)
        objects[x].draw(context);

    // FIXME: do something (restart? rebound?) if the ball scores a point.
    // FIXME: maybe draw text on the canvas with the score?

	//Player's side of the game screen.
	if (ball.x < 0) {
		computer_score += 1;
		console.log("Computer score: " + computer_score);
		ball.x = canvas.width / 2;
		ball.y = canvas.height / 2;	
	}
	
	//Computer's side.
	if (ball.x > canvas.width) {
		player_score += 1;
		console.log("Player score: " + player_score);
		ball.x = canvas.width / 2;
		ball.y = canvas.height / 2;
	}
}


function run_computer_ai() {
    // FIXME: set computer_paddle.velocity_y to something based on
    // the ball position and direction.

    // Try uncommenting this:
    // computer_paddle.velocity_y = -computer_paddle.speed;
	
	if (ball.y > computer_paddle.y) {
		computer_paddle.velocity_y = computer_paddle.speed - 0.25;
	}

	if (ball.y < computer_paddle.y) {
		computer_paddle.velocity_y = -computer_paddle.speed + 0.25;
	}
}

// Runs once at the beginning to set everything up.
function init() {
    canvas = document.getElementById("game");
    canvas.width = 600;
    canvas.height = 400;
    context = canvas.getContext('2d');

    ball = new Ball();
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.velocity_x = -0.2;
    ball.velocity_y = 0.3;

	// Add score displays.
	player_score = 0
	computer_score = 0
	p_score = new PlayerScore();
	c_score = new ComputerScore();

    // Player paddle on the left, centered vertically.
    player_paddle = new Paddle();
    player_paddle.x = 10;
    player_paddle.y = canvas.height / 2 - player_paddle.height / 2;
    player_paddle.reflect_dir = 1;

    // Computer paddle on the right, centered vertically.
    computer_paddle = new Paddle();
    computer_paddle.x = canvas.width - 10 - computer_paddle.width;
    computer_paddle.y = canvas.height / 2 - player_paddle.height / 2;
    computer_paddle.reflect_dir = -1;

    paddles.length = 0;
    paddles.push(player_paddle);
    paddles.push(computer_paddle);

    balls.length = 0;
    balls.push(ball);

    objects = balls.concat(paddles);

    // Player input.
    document.addEventListener("keydown", function(e) {
        if (e.keyCode == 38) {
            player_paddle.velocity_y = -player_paddle.speed;
        } else if (e.keyCode == 40) {
            player_paddle.velocity_y = player_paddle.speed;
        }
    }, false);
    document.addEventListener("keyup", function(e) {
        if (e.keyCode == 38 || e.keyCode == 40) {
            player_paddle.velocity_y = 0;
        }
    }, false);

    last_time = undefined;

    // Start the game loop.
    animate();
}

function checkCollision(ball, paddle) {
    // If ball higher or lower than the paddle, no collision.
    if (ball.y + ball.height < paddle.y || ball.y > paddle.y + paddle.height)
        return false;

    // If ball left or right of the paddle, no collision.
    if (ball.x + ball.width < paddle.x || ball.x > paddle.x + paddle.width)
        return false;

    // If we get here, ball collides with paddle.  Send it off in the
    // right direction.
    ball.velocity_x = Math.abs(ball.velocity_x) * paddle.reflect_dir;
    return true;
}
