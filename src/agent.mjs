// ============================================================
//  Your agent lives here!
//
//  Right now it only echoes. In Module 1 you will replace all
//  of the code in this file with a real AI agent — follow the
//  workshop guide.
// ============================================================

export async function* answerWith(message) {
  yield { type: "token", text: "I'm not an agent yet — finish Module 1 to bring me to life!" };
}
