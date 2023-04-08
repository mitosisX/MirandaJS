const app = {
  readFile(file) {
    return __file.read_file(file);
  },
  writeFile(file, content) {
    __file.write_file(file, content);
  },
  createFile(file) {
    __file.create_file(file);
  },
  appendFile(file, content) {
    __file.append_file(file, content);
  },
  writeBytes(file, bytes) {
    __file.writeBytes(file, bytes);
  },
  // about popup
  aPopup(parent, title, message) {
    __aPopup(parent, title, message);
  },
  // critical popup
  cPopup(parent, title, message) {
    __cPopup(parent, title, message);
  },
  // information popup
  iPopup(parent, title, message) {
    __iPopup(parent, title, message);
  },
  // question popup
  qPopup(parent, title, message, buttons) {
    __qPopup(parent, title, message, buttons);
  },
  // warning popup
  wPopup(parent, title, message) {
    __wPopup(parent, title, message);
  },
  execute(script) {
    __js_execute(script);
  },
  setClipboardText(text) {
    __clipboard.setText(text);
  },
  getClipboardText() {
    __clipboard.getText();
  },
};
