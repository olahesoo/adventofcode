(ns solutions.2023.03.olahesoo.solution
  (:require [clojure.string :as str]))

(def sample-input-path "2023/03/olahesoo/sample_input")
(def input-path "2023/03/olahesoo/input")

(defn get-input [path]
  (->> (slurp path)
       (str/split-lines)
       (list*)))

(defrecord PartNumber [line-nr start value])
(defrecord SchemaSymbol [line-nr index value])

(defn parse-line-impl [line-nr zipped-line part-buffer]
  (if-let [x (first zipped-line)]
    (if-let [n (re-matches #"\d" (str (second x)))]
      (parse-line-impl line-nr (next zipped-line) (update (or part-buffer
                                                              (PartNumber. line-nr (first x) 0))
                                                          :value
                                                          #(+ (Integer/parseInt n) (* 10 %))))
      (if (= (second x) \.)
        (concat (if part-buffer [part-buffer] [])
                (parse-line-impl line-nr (next zipped-line) nil))
        ;; not digit or empty, therefore symbol
        (concat (if part-buffer [part-buffer])
                [(SchemaSymbol. line-nr (first x) (second x))]
                (parse-line-impl line-nr (next zipped-line) nil))))
    (if part-buffer
      [part-buffer]
      [])))

(defn parse-line [line-nr line] (parse-line-impl line-nr (sort (zipmap (range) line)) nil))

(defn parse-data [input]
  (->> (zipmap (range) input)
       (map #(parse-line (first %) (second %)))
       (flatten)))

(def sample-data (parse-data (get-input sample-input-path)))

(defn adjacent-coords [part-number]
  (for [x (range (- (:line-nr part-number) 1)
                 (+ (:line-nr part-number) 2))
        y (range (- (:start part-number) 1)
                 (+ (:start part-number) (count (str (:value part-number))) 1))]
    [x y]))

(defn is-adjacent [part-number schema-symbol]
  (some #(= % [(:line-nr schema-symbol) (:index schema-symbol)])
        (adjacent-coords part-number)))

(defn adjacent-parts [data]
  (let [part-numbers (filter #(= (type %) PartNumber) data)
        schema-symbols (->> (filter #(= (type %) SchemaSymbol) data))]
    (filter (fn [part-number]
              (some #(is-adjacent part-number %)
                    schema-symbols))
            part-numbers)))

(defn solve-1 [path]
  (->> (get-input path)
       (parse-data)
       (adjacent-parts)
       (map :value)
       (apply +)))

(defn gears [data]
  (let [part-numbers (filter #(= (type %) PartNumber) data)
        schema-symbols (->> (filter #(= (type %) SchemaSymbol) data))]
    (->> (filter #(= (:value %) \*) schema-symbols)
         (map (fn [schema-symbol]
                (array-map schema-symbol (filter
                                           #(is-adjacent % schema-symbol)
                                           part-numbers))))
         (apply merge)
         (filter #(= (count (second %)) 2)))))

(defn solve-2 [path]
  (->> (get-input path)
       (parse-data)
       (gears)
       (vals)
       (map #(map :value %))
       (map #(apply * %))
       (apply +)))
