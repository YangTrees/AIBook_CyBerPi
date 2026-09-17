const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const courseDir = path.join(root, 'AI编程探险课_CyberPi', '_parts');
const detail = JSON.parse(fs.readFileSync(path.join(__dirname, '_lessons_data_fixed.json'), 'utf8'));

for (let group = 1; group <= 4; group++) {
  const file = path.join(courseDir, `data${group}.js`);
  let source = fs.readFileSync(file, 'utf8');
  const first = (group - 1) * 8 + 1;
  const last = group * 8;

  for (let id = first; id <= last; id++) {
    const steps = detail[String(id)].steps;
    const value = JSON.stringify(steps, null, 0);
    const lessonStart = source.indexOf(`  id:${id},`);
    if (lessonStart < 0) throw new Error(`Lesson ${id} not found in ${file}`);
    const nextLesson = source.indexOf('\n{\n  id:', lessonStart + 1);
    const lessonEnd = nextLesson < 0 ? source.lastIndexOf('\n];') : nextLesson;
    const lesson = source.slice(lessonStart, lessonEnd);
    const updated = lesson.replace(/  steps:\[[\s\S]*?\],\r?\n  challenge:/, `  steps:${value},\n  challenge:`);
    if (lesson === updated) throw new Error(`Steps for lesson ${id} were not replaced`);
    source = source.slice(0, lessonStart) + updated + source.slice(lessonEnd);
  }

  fs.writeFileSync(file, source, 'utf8');
}

console.log('Synced detailed implementation steps for 32 lessons.');
