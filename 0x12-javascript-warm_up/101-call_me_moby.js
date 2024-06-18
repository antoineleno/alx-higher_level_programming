#!/usr/bin/node
exports.call_me_moby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
