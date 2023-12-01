(ns solutions.2022.01.olahesoo.solution
  (:require [clojure.string :as str]))

(defn get-input [path]
  (->> (slurp path)
       (str/split-lines)
       (list*)))

(def sample-input
  (get-input "2022/01/olahesoo/sample_input"))

(def input
  (get-input "2022/01/olahesoo/input"))

(defn split-input-impl [in out]
  (if (empty? in)
    out
    (if (= (first in) "")
      (split-input-impl (rest in) (cons () out))
      (split-input-impl (rest in) (cons (cons (Integer/parseInt (first in)) (first out)) (rest out))))))

(defn split-input [in] (split-input-impl in ()))

(defn get-sums [elves]
  (map #(reduce + %) elves))

(defn solve-1 [input]
  (->> (split-input input)
       (get-sums)
       (apply max)))

(defn solve-2 [input]
  (->> (split-input input)
       (get-sums)
       (sort >)
       (take 3)
       (apply +)))