var gulp = require('gulp');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var gutil = require('gulp-util');

gulp.task('minify', function(){
	gulp.src(['./Controller/*.js', '!./Controller/*.min.js'])
	.pipe(uglify())
	.on('error', gutil.log)
	.pipe(rename({suffix: '.min'}))
	.pipe(gulp.dest('./Controller/'));

	gulp.src(['./*.js', '!./*.min.js', '!./gulpfile.js'])
	.pipe(uglify())
	.on('error', gutil.log)
	.pipe(rename({suffix: '.min'}))
	.pipe(gulp.dest('./'));
});