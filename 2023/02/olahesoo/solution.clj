(ns solutions.2023.02.olahesoo.solution
  (:require [clojure.string :as str]))

(def sample-input-path "2023/02/olahesoo/sample_input")
(def input-path "2023/02/olahesoo/input")

(defn get-input [path]
  (->> (slurp path)
       (str/split-lines)
       (list*)))

(defn convert-map [cubes]
  (hash-map (second cubes) (Integer/parseInt (first cubes))))

(defn parse-set [set-str]
  (->> (str/split set-str #", ")
       (map #(convert-map (str/split % #" ")))
       (apply merge)))

(defn parse-sets [sets-str]
  (->> (str/split sets-str #"; ")
       (map parse-set)))

(defn parse-game [game-str]
  (let [match (re-matches #"Game (\d+): (.*)" game-str)]
    {:game-id (Integer/parseInt (get match 1))
     :game-sets (parse-sets (get match 2))}))

(def limits {"red" 12
             "green" 13
             "blue" 14})

(defn compare-limits [limits dice-sets]
  (->> (for [limit limits
             dice-set dice-sets]
         (if-let [dice (dice-set (first limit))]
           (<= dice (second limit))
           true))
       (every? identity)))

(defn solve [path]
  (->> (get-input path)
       (map parse-game)
       (filter #(compare-limits limits (:game-sets %)))
       (map :game-id)
       (apply +)))

(defn solve-2 [path]
  (->> (get-input path)
       (map parse-game)
       (map :game-sets)
       (map #(apply merge-with max %))
       (map #(reduce * (vals %)))
       (apply +)))
