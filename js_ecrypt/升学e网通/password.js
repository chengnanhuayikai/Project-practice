md5 = function(e, t, n) {
    !function(t, r) {
        e.exports = r(n(328))
    }(0, function(e) {
        return function(t) {
            var n = e
              , r = n.lib
              , o = r.WordArray
              , a = r.Hasher
              , i = n.algo
              , u = [];
            !function() {
                for (var e = 0; e < 64; e++)
                    u[e] = 4294967296 * t.abs(t.sin(e + 1)) | 0
            }();
            var c = i.MD5 = a.extend({
                _doReset: function() {
                    this._hash = new o.init([1732584193, 4023233417, 2562383102, 271733878])
                },
                _doProcessBlock: function(e, t) {
                    for (var n = 0; n < 16; n++) {
                        var r = t + n
                          , o = e[r];
                        e[r] = 16711935 & (o << 8 | o >>> 24) | 4278255360 & (o << 24 | o >>> 8)
                    }
                    var a = this._hash.words
                      , i = e[t + 0]
                      , c = e[t + 1]
                      , d = e[t + 2]
                      , h = e[t + 3]
                      , y = e[t + 4]
                      , v = e[t + 5]
                      , m = e[t + 6]
                      , g = e[t + 7]
                      , b = e[t + 8]
                      , A = e[t + 9]
                      , E = e[t + 10]
                      , w = e[t + 11]
                      , C = e[t + 12]
                      , O = e[t + 13]
                      , P = e[t + 14]
                      , x = e[t + 15]
                      , S = a[0]
                      , j = a[1]
                      , k = a[2]
                      , T = a[3];
                    j = p(j = p(j = p(j = p(j = f(j = f(j = f(j = f(j = l(j = l(j = l(j = l(j = s(j = s(j = s(j = s(j, k = s(k, T = s(T, S = s(S, j, k, T, i, 7, u[0]), j, k, c, 12, u[1]), S, j, d, 17, u[2]), T, S, h, 22, u[3]), k = s(k, T = s(T, S = s(S, j, k, T, y, 7, u[4]), j, k, v, 12, u[5]), S, j, m, 17, u[6]), T, S, g, 22, u[7]), k = s(k, T = s(T, S = s(S, j, k, T, b, 7, u[8]), j, k, A, 12, u[9]), S, j, E, 17, u[10]), T, S, w, 22, u[11]), k = s(k, T = s(T, S = s(S, j, k, T, C, 7, u[12]), j, k, O, 12, u[13]), S, j, P, 17, u[14]), T, S, x, 22, u[15]), k = l(k, T = l(T, S = l(S, j, k, T, c, 5, u[16]), j, k, m, 9, u[17]), S, j, w, 14, u[18]), T, S, i, 20, u[19]), k = l(k, T = l(T, S = l(S, j, k, T, v, 5, u[20]), j, k, E, 9, u[21]), S, j, x, 14, u[22]), T, S, y, 20, u[23]), k = l(k, T = l(T, S = l(S, j, k, T, A, 5, u[24]), j, k, P, 9, u[25]), S, j, h, 14, u[26]), T, S, b, 20, u[27]), k = l(k, T = l(T, S = l(S, j, k, T, O, 5, u[28]), j, k, d, 9, u[29]), S, j, g, 14, u[30]), T, S, C, 20, u[31]), k = f(k, T = f(T, S = f(S, j, k, T, v, 4, u[32]), j, k, b, 11, u[33]), S, j, w, 16, u[34]), T, S, P, 23, u[35]), k = f(k, T = f(T, S = f(S, j, k, T, c, 4, u[36]), j, k, y, 11, u[37]), S, j, g, 16, u[38]), T, S, E, 23, u[39]), k = f(k, T = f(T, S = f(S, j, k, T, O, 4, u[40]), j, k, i, 11, u[41]), S, j, h, 16, u[42]), T, S, m, 23, u[43]), k = f(k, T = f(T, S = f(S, j, k, T, A, 4, u[44]), j, k, C, 11, u[45]), S, j, x, 16, u[46]), T, S, d, 23, u[47]), k = p(k, T = p(T, S = p(S, j, k, T, i, 6, u[48]), j, k, g, 10, u[49]), S, j, P, 15, u[50]), T, S, v, 21, u[51]), k = p(k, T = p(T, S = p(S, j, k, T, C, 6, u[52]), j, k, h, 10, u[53]), S, j, E, 15, u[54]), T, S, c, 21, u[55]), k = p(k, T = p(T, S = p(S, j, k, T, b, 6, u[56]), j, k, x, 10, u[57]), S, j, m, 15, u[58]), T, S, O, 21, u[59]), k = p(k, T = p(T, S = p(S, j, k, T, y, 6, u[60]), j, k, w, 10, u[61]), S, j, d, 15, u[62]), T, S, A, 21, u[63]),
                    a[0] = a[0] + S | 0,
                    a[1] = a[1] + j | 0,
                    a[2] = a[2] + k | 0,
                    a[3] = a[3] + T | 0
                },
                _doFinalize: function() {
                    var e = this._data
                      , n = e.words
                      , r = 8 * this._nDataBytes
                      , o = 8 * e.sigBytes;
                    n[o >>> 5] |= 128 << 24 - o % 32;
                    var a = t.floor(r / 4294967296)
                      , i = r;
                    n[15 + (o + 64 >>> 9 << 4)] = 16711935 & (a << 8 | a >>> 24) | 4278255360 & (a << 24 | a >>> 8),
                    n[14 + (o + 64 >>> 9 << 4)] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8),
                    e.sigBytes = 4 * (n.length + 1),
                    this._process();
                    for (var u = this._hash, c = u.words, s = 0; s < 4; s++) {
                        var l = c[s];
                        c[s] = 16711935 & (l << 8 | l >>> 24) | 4278255360 & (l << 24 | l >>> 8)
                    }
                    return u
                },
                clone: function() {
                    var e = a.clone.call(this);
                    return e._hash = this._hash.clone(),
                    e
                }
            });
            function s(e, t, n, r, o, a, i) {
                var u = e + (t & n | ~t & r) + o + i;
                return (u << a | u >>> 32 - a) + t
            }
            function l(e, t, n, r, o, a, i) {
                var u = e + (t & r | n & ~r) + o + i;
                return (u << a | u >>> 32 - a) + t
            }
            function f(e, t, n, r, o, a, i) {
                var u = e + (t ^ n ^ r) + o + i;
                return (u << a | u >>> 32 - a) + t
            }
            function p(e, t, n, r, o, a, i) {
                var u = e + (n ^ (t | ~r)) + o + i;
                return (u << a | u >>> 32 - a) + t
            }
            n.MD5 = a._createHelper(c),
            n.HmacMD5 = a._createHmacHelper(c)
        }(Math),
        e.MD5
    })
};
en = function(e, t, n) {
    !function(t, n) {
        e.exports = n()
    }(0, function() {
        var e = e || function(e, t) {
            var n = Object.create || function() {
                function e() {}
                return function(t) {
                    var n;
                    return e.prototype = t,
                    n = new e,
                    e.prototype = null,
                    n
                }
            }()
              , r = {}
              , o = r.lib = {}
              , a = o.Base = {
                extend: function(e) {
                    var t = n(this);
                    return e && t.mixIn(e),
                    t.hasOwnProperty("init") && this.init !== t.init || (t.init = function() {
                        t.$super.init.apply(this, arguments)
                    }
                    ),
                    t.init.prototype = t,
                    t.$super = this,
                    t
                },
                create: function() {
                    var e = this.extend();
                    return e.init.apply(e, arguments),
                    e
                },
                init: function() {},
                mixIn: function(e) {
                    for (var t in e)
                        e.hasOwnProperty(t) && (this[t] = e[t]);
                    e.hasOwnProperty("toString") && (this.toString = e.toString)
                },
                clone: function() {
                    return this.init.prototype.extend(this)
                }
            }
              , i = o.WordArray = a.extend({
                init: function(e, t) {
                    e = this.words = e || [],
                    this.sigBytes = void 0 != t ? t : 4 * e.length
                },
                toString: function(e) {
                    return (e || c).stringify(this)
                },
                concat: function(e) {
                    var t = this.words
                      , n = e.words
                      , r = this.sigBytes
                      , o = e.sigBytes;
                    if (this.clamp(),
                    r % 4)
                        for (var a = 0; a < o; a++) {
                            var i = n[a >>> 2] >>> 24 - a % 4 * 8 & 255;
                            t[r + a >>> 2] |= i << 24 - (r + a) % 4 * 8
                        }
                    else
                        for (a = 0; a < o; a += 4)
                            t[r + a >>> 2] = n[a >>> 2];
                    return this.sigBytes += o,
                    this
                },
                clamp: function() {
                    var t = this.words
                      , n = this.sigBytes;
                    t[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
                    t.length = e.ceil(n / 4)
                },
                clone: function() {
                    var e = a.clone.call(this);
                    return e.words = this.words.slice(0),
                    e
                },
                random: function(t) {
                    for (var n, r = [], o = function(t) {
                        t = t;
                        var n = 987654321
                          , r = 4294967295;
                        return function() {
                            var o = ((n = 36969 * (65535 & n) + (n >> 16) & r) << 16) + (t = 18e3 * (65535 & t) + (t >> 16) & r) & r;
                            return o /= 4294967296,
                            (o += .5) * (e.random() > .5 ? 1 : -1)
                        }
                    }, a = 0; a < t; a += 4) {
                        var u = o(4294967296 * (n || e.random()));
                        n = 987654071 * u(),
                        r.push(4294967296 * u() | 0)
                    }
                    return new i.init(r,t)
                }
            })
              , u = r.enc = {}
              , c = u.Hex = {
                stringify: function(e) {
                    for (var t = e.words, n = e.sigBytes, r = [], o = 0; o < n; o++) {
                        var a = t[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                        r.push((a >>> 4).toString(16)),
                        r.push((15 & a).toString(16))
                    }
                    return r.join("")
                },
                parse: function(e) {
                    for (var t = e.length, n = [], r = 0; r < t; r += 2)
                        n[r >>> 3] |= parseInt(e.substr(r, 2), 16) << 24 - r % 8 * 4;
                    return new i.init(n,t / 2)
                }
            }
              , s = u.Latin1 = {
                stringify: function(e) {
                    for (var t = e.words, n = e.sigBytes, r = [], o = 0; o < n; o++) {
                        var a = t[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                        r.push(String.fromCharCode(a))
                    }
                    return r.join("")
                },
                parse: function(e) {
                    for (var t = e.length, n = [], r = 0; r < t; r++)
                        n[r >>> 2] |= (255 & e.charCodeAt(r)) << 24 - r % 4 * 8;
                    return new i.init(n,t)
                }
            }
              , l = u.Utf8 = {
                stringify: function(e) {
                    try {
                        return decodeURIComponent(escape(s.stringify(e)))
                    } catch (t) {
                        throw new Error("Malformed UTF-8 data")
                    }
                },
                parse: function(e) {
                    return s.parse(unescape(encodeURIComponent(e)))
                }
            }
              , f = o.BufferedBlockAlgorithm = a.extend({
                reset: function() {
                    this._data = new i.init,
                    this._nDataBytes = 0
                },
                _append: function(e) {
                    "string" == typeof e && (e = l.parse(e)),
                    this._data.concat(e),
                    this._nDataBytes += e.sigBytes
                },
                _process: function(t) {
                    var n = this._data
                      , r = n.words
                      , o = n.sigBytes
                      , a = this.blockSize
                      , u = o / (4 * a)
                      , c = (u = t ? e.ceil(u) : e.max((0 | u) - this._minBufferSize, 0)) * a
                      , s = e.min(4 * c, o);
                    if (c) {
                        for (var l = 0; l < c; l += a)
                            this._doProcessBlock(r, l);
                        var f = r.splice(0, c);
                        n.sigBytes -= s
                    }
                    return new i.init(f,s)
                },
                clone: function() {
                    var e = a.clone.call(this);
                    return e._data = this._data.clone(),
                    e
                },
                _minBufferSize: 0
            })
              , p = (o.Hasher = f.extend({
                cfg: a.extend(),
                init: function(e) {
                    this.cfg = this.cfg.extend(e),
                    this.reset()
                },
                reset: function() {
                    f.reset.call(this),
                    this._doReset()
                },
                update: function(e) {
                    return this._append(e),
                    this._process(),
                    this
                },
                finalize: function(e) {
                    return e && this._append(e),
                    this._doFinalize()
                },
                blockSize: 16,
                _createHelper: function(e) {
                    return function(t, n) {
                        return new e.init(n).finalize(t)
                    }
                },
                _createHmacHelper: function(e) {
                    return function(t, n) {
                        return new p.HMAC.init(e,n).finalize(t)
                    }
                }
            }),
            r.algo = {});
            return r
        }(Math);
        return e
    })
};


console.log(en.parse("11111"))
// https://web.ewt360.com/register/#/login?_k=4plq2g  未破解
