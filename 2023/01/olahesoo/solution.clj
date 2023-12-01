(ns solutions.2023.01.olahesoo.solution
  (:require [clojure.string :as str]))

(def sample-input-path "2023/01/olahesoo/sample_input")
(def input-path "2023/01/olahesoo/input")

(defn get-input [path]
  (->> (slurp path)
       (str/split-lines)
       (list*)))

(defn get-first-digit [s]
  (get (re-matches #".*?(\d).*" s) 1))

(defn get-last-digit [s]
  (get (re-matches #".*(\d).*" s) 1))

(defn get-first-digit-2 [s]
  (get (re-matches #".*?(\d|one|two|three|four|five|six|seven|eight|nine).*" s) 1))

(defn get-last-digit-2 [s]
  (get (re-matches #".*(\d|one|two|three|four|five|six|seven|eight|nine).*" s) 1))

(defn parse-digit [s]
  (try
    (Integer/parseInt s)
    (catch NumberFormatException e
      (case s
        "one" 1
        "two" 2
        "three" 3
        "four" 4
        "five" 5
        "six" 6
        "seven" 7
        "eight" 8
        "nine" 9))))

(defn get-calibration-number [s]
  (Integer/parseInt (str/join [(get-first-digit s) (get-last-digit s)])))

(defn get-calibration-number-2 [s]
  (+ (* 10 (parse-digit (get-first-digit-2 s))) (parse-digit (get-last-digit-2 s))))

(defn solve-1 [path]
  (->> (get-input path)
       (map get-calibration-number)
       (apply +)))

(defn solve-2 [path]
  (->> (get-input path)
       (map get-calibration-number-2)
       (apply +)))