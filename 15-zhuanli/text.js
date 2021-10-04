function y(t) {
            return void 0 === t && (t = 6),
            Math.random().toString(36).substring(2, t + 2)
        }

function c(t) {
        var e = this.currentSearchConceptID
          , n = this.getSearchConceptID()
          , r = this.getUserActionID(t)
          , i = function(t) {
            void 0 === t && (t = {}),
            t.reset && (b = 0);
            var e = ""
              , n = (b++).toString()
              , r = t.sequenceLength || 6;
            if (n.length < r) {
                var i = r - n.length;
                e = new Array(i).fill("0").join("")
            }
            return "" + e + n
        }({
            reset: n !== e,
            sequenceLength: 6
        });
        return this.sessionID + "-" + n + "-" + r + "-" + i
    }


function b(t, e) {
            if (!t)
                return "";
            var n = function(t) {
                switch (t.arrayFormat) {
                case "index":
                    return function(e, n, r) {
                        return null === n ? [l(e, t), "[", r, "]"].join("") : [l(e, t), "[", l(r, t), "]=", l(n, t)].join("")
                    }
                    ;
                case "bracket":
                    return function(e, n) {
                        return null === n ? [l(e, t), "[]"].join("") : [l(e, t), "[]=", l(n, t)].join("")
                    }
                    ;
                default:
                    return function(e, n) {
                        return null === n ? l(e, t) : [l(e, t), "=", l(n, t)].join("")
                    }
                }
            }(e = Object.assign({
                encode: !0,
                strict: !0,
                arrayFormat: "none"
            }, e))
              , r = Object.keys(t);
            return !1 !== e.sort && r.sort(e.sort),
            r.map((function(r) {
                var o = t[r];
                if (void 0 === o)
                    return "";
                if (null === o)
                    return l(r, e);
                if (Array.isArray(o)) {
                    var a, s = [], c = i(o.slice());
                    try {
                        for (c.s(); !(a = c.n()).done; ) {
                            var u = a.value;
                            void 0 !== u && s.push(n(r, u, s.length))
                        }
                    } catch (t) {
                        c.e(t)
                    } finally {
                        c.f()
                    }
                    return s.join("&")
                }
                return l(r, e) + "=" + l(o, e)
            }
            )).filter((function(t) {
                return t.length > 0
            }
            )).join("&")
        }


function d(t, e) {
                void 0 === e && (e = {});
                var n = Object(d.a)(f.a, {}, [{
                    url: t
                }, this.defaultSettings, e])
                  , r = o()(n);
                return this._errorHandler && r.catch(this._errorHandler),
                r
            }


function f(t) {
                var e = this;
                return !!this.debouncedStatistic[t] || (this.debouncedStatistic[t] = !0,
                setTimeout((function() {
                    return e.debouncedStatistic[t] = !1
                }
                ), 600),
                !1)
            }


function a() {
        var n = {event: "familySelect_065720642_BibliographicData-BibliographicData", lgCC: "en_EP"};
        var r = n ? "&" + Object(b())(n, {
            sort: !1
        }) : ""
          , i = "/patent/?EPOTraceID=" + y() + "-" + y() + r;
        if (!("keyboardClick_ArrowDown" === n.event && f("keyboardClick_ArrowDown") || "keyboardClick_ArrowUp" === n.event && f("keyboardClick_ArrowUp") || -1 !== n.event.indexOf("familySelect_") && f("familySelect")))
            return d(i, {
                method: "head",
                headers: {
                    "EPO-Trace-Id": c(i)
                }
            })
}