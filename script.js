let canvas;
const dt = 0.001;

let N = 500;
let speed = 1000;
let r = 20;
let noise = Math.PI * 0.01;

let particles = [];
let v_avg_x, v_avg_y, v_avg;

let sim_width, sim_height;
let noise_slider, r_slider, toggle_button, reset_button;

let looping = true;

let time_series = Array(1000).fill(0);

class Particle {
    constructor(x, y, v, theta, size=5) {
        this.x = x;
        this.y = y;
        this.v = v;
        this.theta = theta;
        this.size = size;
    }

    update() {
        let avgTheta = 0;
        let count = 0;

        let avgX = 0;
        let avgY = 0;
        let separationX = 0;
        let separationY = 0;

        for (const particle of particles) {
            const dx = particle.x - this.x;
            const dy = particle.y - this.y;
            const distanceSq = (dx * dx) + (dy * dy);

            if (distanceSq < r*r) { // interaction radius
                avgTheta += particle.theta;
                avgX += particle.x;
                avgY += particle.y;

                if (distanceSq < 3*this.size*3*this.size) { // separation radius
                    separationX += dx;
                    separationY += dy;
                }
                count++;
            }
        }

        if (count > 0) {
            avgTheta /= count;
            avgX /= count;
            avgY /= count;

            // // alignment, cohesion, and separation
            // let headingX = r*Math.cos(avgTheta) + (avgX - this.x) - 0.5*separationX;
            // let headingY = r*Math.sin(avgTheta) + (avgY - this.y) - 0.5*separationY;
            // this.theta = Math.atan2(headingY, headingX) + random(-noise, noise);

            // alignment only
            this.theta = avgTheta + random(-noise, noise); // adding some noise
        }
    }

    move() {
        this.x += this.v * dt * Math.cos(this.theta);
        this.y += this.v * dt * Math.sin(this.theta);

        // Periodic boundary conditions
        if (this.x < 0) this.x += sim_width;
        if (this.x > sim_width) this.x -= sim_width;
        if (this.y < 0) this.y += sim_height;
        if (this.y > sim_height) this.y -= sim_height;
    }

    show() {
        // ellipse(this.x, this.y, this.size, this.size);

        push();
        translate(this.x, this.y);
        rotate(this.theta);
        beginShape();
        vertex(-this.size, -this.size / 2);
        vertex(this.size, 0);
        vertex(-this.size, this.size / 2);
        endShape(CLOSE);
        pop();
    }
}


function setup() {
    canvas = createCanvas(windowWidth, windowHeight);
    sim_width = windowWidth, sim_height = 0.66* windowHeight;
    background(0);

    noise_slider = createSlider(0, 2*Math.PI, noise, 0);
    noise_slider.position(150, sim_height+15);
    noise_slider.size(200);

    r_slider = createSlider(0, 100, r, 1);
    r_slider.position(150, sim_height+40);
    r_slider.size(200);

    toggle_button = createButton('Toggle Simulation');
    toggle_button.position(150, sim_height+65);
    toggle_button.size(200);
    toggle_button.mousePressed(() => {
        if (looping) {
            noLoop();
            looping = false;
        }
        else {
            loop();
            looping = true;
        }
    });

    reset_button = createButton('Reset Simulation');
    reset_button.position(150, sim_height+90);
    reset_button.size(200);
    reset_button.mousePressed(() => {
        particles = [];
        for (let i = 0; i < N; i++) {
            particles.push(new Particle(random(0, sim_width), random(0, sim_height), speed, random(2 * Math.PI)));
        }
        time_series = Array(1000).fill(0);
        draw();
    });

    for (let i = 0; i < N; i++) {
        particles.push(new Particle(random(0, sim_width), random(0, sim_height), speed, random(2 * Math.PI)));
    }
}

function draw() {
    background(0);

    stroke(0);
    strokeWeight(0.5);
    fill(255);
    for (const particle of particles) {
        particle.update();
        particle.move();
        particle.show();
    }

    draw_noise_slider();
    noise = noise_slider.value();
    draw_r_slider();
    r = r_slider.value();

    calculate_v_avg();
    time_series.shift();
    time_series.push(v_avg);

    stroke(255); strokeWeight(1);
    line(0, sim_height, sim_width, sim_height);

    stroke(255); strokeWeight(1);
    line(sim_width/4, sim_height, sim_width/4, windowHeight);

    draw_graph();
}

function draw_noise_slider() {
    stroke(255); fill(255); textSize(16);
    text('Orientation Noise', 10, sim_height+15+15);
}

function draw_r_slider() {
    stroke(255); fill(255); textSize(16);
    text('Interaction Radius', 10, sim_height+40+15);
}

function draw_graph() {
    line(windowWidth/4 + 50, sim_height+25, windowWidth/4 + 50, windowHeight-25);
    line(windowWidth/4 + 50, windowHeight-50, windowWidth/4 + 50 + 1000 + 25, windowHeight-50);

    stroke(255); fill(255); strokeWeight(1);
    for (let i = 0; i < time_series.length; i++) {
        point(windowWidth/4 + 50 + i, windowHeight - 50 - lerp(0, windowHeight-sim_height-100, time_series[i]));
    }
    // Draw tick marks on the y-axis
    for (let i = 0; i <= 10; i++) {
        let y = windowHeight - 50 - lerp(0, windowHeight - sim_height - 75, i / 10);
        stroke(255);
        line(windowWidth / 4 + 45, y, windowWidth / 4 + 55, y);
        if (i === 0 || i === 10) {
            noStroke();
            fill(255);
            text((i / 10).toFixed(1), windowWidth / 4 + 15, y + 5);
        }
    }

    // Draw x-axis label
    noStroke();
    fill(255);
    textSize(16);
    text('Time', windowWidth / 4 + 50 + 500, windowHeight - 30);

    // Draw y-axis label
    push();
    translate(windowWidth / 4 + 30, sim_height+47.5 + (windowHeight - sim_height) / 2);
    rotate(-PI / 2);
    text('Average Velocity', 0, 0);
    pop();

    text(v_avg.toFixed(2),
        windowWidth/4 + 50 + 1000 - 25,
        windowHeight - 50 - lerp(0, windowHeight-sim_height-100, time_series[time_series.length-1]) - 10
    );
}

function calculate_v_avg() {
    v_avg_x = 0, v_avg_y = 0, v_avg = 0;
    for (const particle of particles) {
        v_avg_x += particle.v * Math.cos(particle.theta);
        v_avg_y += particle.v * Math.sin(particle.theta);
    }
    v_avg_x /= N, v_avg_y /= N;
    v_avg = Math.sqrt(v_avg_x*v_avg_x + v_avg_y*v_avg_y);
    v_avg /= speed;
}


// v_avg vs t, cluster size vs t, polar order vs t
let noise_values = [];
let order_parameters = [];

function calculate_order_parameter() {
    let sum_sin = 0;
    let sum_cos = 0;

    for (const particle of particles) {
        sum_sin += Math.sin(particle.theta);
        sum_cos += Math.cos(particle.theta);
    }

    let order_parameter = Math.sqrt(sum_sin * sum_sin + sum_cos * sum_cos) / N;
    return order_parameter;
}

function record_noise_vs_order() {
    noise_values.push(noise);
    order_parameters.push(calculate_order_parameter());
}

// Call this function at appropriate intervals to record the data
function update_noise_vs_order() {
    if (frameCount % 10 === 0) { // Adjust the interval as needed
        record_noise_vs_order();
    }
}

function draw() {
    background(0);

    stroke(0);
    strokeWeight(0.5);
    fill(255);
    for (const particle of particles) {
        particle.update();
        particle.move();
        particle.show();
    }

    draw_noise_slider();
    noise = noise_slider.value();
    draw_r_slider();
    r = r_slider.value();

    calculate_v_avg();
    time_series.shift();
    time_series.push(v_avg);

    stroke(255); strokeWeight(1);
    line(0, sim_height, sim_width, sim_height);

    stroke(255); strokeWeight(1);
    line(sim_width/4, sim_height, sim_width/4, windowHeight);

    draw_graph();
    update_noise_vs_order();
}

function get_noise_vs_v_avg() {
    let noise_values = [];
    let v_avg_values = [];

    for (let n = 0; n <= 2 * Math.PI; n += 0.1) {
        noise = n;
        for (let i = 0; i < 500; i++) { // Run the simulation for some steps to stabilize
            for (const particle of particles) {
                particle.update();
                particle.move();
            }
        }
        calculate_v_avg();
        noise_values.push(n);
        v_avg_values.push(v_avg);
    }

    console.log('done!');
    console.log(noise_values);
    console.log(v_avg_values);
}

function get_r_vs_v_avg() {
    let r_values = [];
    let v_avg_values = [];

    for (let radius = 0; radius <= 100; radius += 2) {
        r = radius;
        for (let i = 0; i < 500; i++) { // Run the simulation for some steps to stabilize
            for (const particle of particles) {
                particle.update();
                particle.move();
            }
        }
        calculate_v_avg();
        r_values.push(radius);
        v_avg_values.push(v_avg);
    }

    console.log('done!');
    console.log(r_values);
    console.log(v_avg_values);
}

function mousePressed() {
    if (mouseY < sim_height) { // Ensure clicks are within the simulation area
        particles.push(new Particle(mouseX, mouseY, speed, random(2 * Math.PI)));
    }
}
