#!/usr/bin/env Rscript

rm(list=ls(all.names=TRUE))
setwd("~/Dropbox/gradschool/sp19/networks/project/networks-project/theoretical-model/")
require(tidyverse)
require(reshape2)
theme_set(theme_classic() + theme(legend.position="bottom"))

# linear gradient
dat <- read.csv("trial.csv", stringsAsFactors=FALSE, 
                col.names=c("x", "r", 
                            "No.Investment", "No.Resources", "No.Growth", "No.Effective.Growth",
                            "Con.Investment", "Con.Resources", "Con.Growth", "Con.Effective.Growth",
                            "Res.Investment", "Res.Resources", "Res.Growth", "Res.Effective.Growth"))
dat <- dat %>%
  melt(id.vars=c("x", "r")) %>%
  mutate(Investment=factor(variable, labels=c(rep("None", 4), 
                                              rep("Constitutive", 4), 
                                              rep("Responsive", 4))),
         Variable=factor(variable, labels=rep(c("Investment", "Resources", "Growth", "Effective growth"), 3)))

dat %>%
  ggplot(aes(x, value, col=Investment, linetype=Investment)) +
  geom_line() +
  scale_color_brewer(palette="Set1", direction=-1) +
  facet_wrap(~Variable) +
  labs(x="Distance from vessel",
       y="Value")
ggsave("linear.png", units="cm", width=12, height=11)

# exponential gradient
dat <- read.csv("exponential.csv", stringsAsFactors=FALSE, 
                col.names=c("x", "r", 
                            "No.Investment", "No.Resources", "No.Growth", "No.Effective.Growth",
                            "Con.Investment", "Con.Resources", "Con.Growth", "Con.Effective.Growth",
                            "Res.Investment", "Res.Resources", "Res.Growth", "Res.Effective.Growth"))
dat <- dat %>%
  melt(id.vars=c("x", "r")) %>%
  mutate(Investment=factor(variable, labels=c(rep("None", 4), 
                                              rep("Constitutive", 4), 
                                              rep("Responsive", 4))),
         Variable=factor(variable, labels=rep(c("Investment", "Resources", "Growth", "Effective growth"), 3)))

dat %>%
  ggplot(aes(x, value, col=Investment, linetype=Investment)) +
  geom_line() +
  scale_color_brewer(palette="Set1", direction=-1) +
  facet_wrap(~Variable) +
  labs(x="Distance from vessel",
       y="Value")
ggsave("exponential.png", units="cm", width=12, height=11)
