<?php
// DO NOT EDIT! Generated by Protobuf-PHP protoc plugin 1.0
// Source: tabletmanagerdata.proto

namespace Vitess\Proto\Tabletmanagerdata {

  class ApplySchemaResponse extends \DrSlump\Protobuf\Message {

    /**  @var \Vitess\Proto\Tabletmanagerdata\SchemaDefinition */
    public $before_schema = null;
    
    /**  @var \Vitess\Proto\Tabletmanagerdata\SchemaDefinition */
    public $after_schema = null;
    

    /** @var \Closure[] */
    protected static $__extensions = array();

    public static function descriptor()
    {
      $descriptor = new \DrSlump\Protobuf\Descriptor(__CLASS__, 'tabletmanagerdata.ApplySchemaResponse');

      // OPTIONAL MESSAGE before_schema = 1
      $f = new \DrSlump\Protobuf\Field();
      $f->number    = 1;
      $f->name      = "before_schema";
      $f->type      = \DrSlump\Protobuf::TYPE_MESSAGE;
      $f->rule      = \DrSlump\Protobuf::RULE_OPTIONAL;
      $f->reference = '\Vitess\Proto\Tabletmanagerdata\SchemaDefinition';
      $descriptor->addField($f);

      // OPTIONAL MESSAGE after_schema = 2
      $f = new \DrSlump\Protobuf\Field();
      $f->number    = 2;
      $f->name      = "after_schema";
      $f->type      = \DrSlump\Protobuf::TYPE_MESSAGE;
      $f->rule      = \DrSlump\Protobuf::RULE_OPTIONAL;
      $f->reference = '\Vitess\Proto\Tabletmanagerdata\SchemaDefinition';
      $descriptor->addField($f);

      foreach (self::$__extensions as $cb) {
        $descriptor->addField($cb(), true);
      }

      return $descriptor;
    }

    /**
     * Check if <before_schema> has a value
     *
     * @return boolean
     */
    public function hasBeforeSchema(){
      return $this->_has(1);
    }
    
    /**
     * Clear <before_schema> value
     *
     * @return \Vitess\Proto\Tabletmanagerdata\ApplySchemaResponse
     */
    public function clearBeforeSchema(){
      return $this->_clear(1);
    }
    
    /**
     * Get <before_schema> value
     *
     * @return \Vitess\Proto\Tabletmanagerdata\SchemaDefinition
     */
    public function getBeforeSchema(){
      return $this->_get(1);
    }
    
    /**
     * Set <before_schema> value
     *
     * @param \Vitess\Proto\Tabletmanagerdata\SchemaDefinition $value
     * @return \Vitess\Proto\Tabletmanagerdata\ApplySchemaResponse
     */
    public function setBeforeSchema(\Vitess\Proto\Tabletmanagerdata\SchemaDefinition $value){
      return $this->_set(1, $value);
    }
    
    /**
     * Check if <after_schema> has a value
     *
     * @return boolean
     */
    public function hasAfterSchema(){
      return $this->_has(2);
    }
    
    /**
     * Clear <after_schema> value
     *
     * @return \Vitess\Proto\Tabletmanagerdata\ApplySchemaResponse
     */
    public function clearAfterSchema(){
      return $this->_clear(2);
    }
    
    /**
     * Get <after_schema> value
     *
     * @return \Vitess\Proto\Tabletmanagerdata\SchemaDefinition
     */
    public function getAfterSchema(){
      return $this->_get(2);
    }
    
    /**
     * Set <after_schema> value
     *
     * @param \Vitess\Proto\Tabletmanagerdata\SchemaDefinition $value
     * @return \Vitess\Proto\Tabletmanagerdata\ApplySchemaResponse
     */
    public function setAfterSchema(\Vitess\Proto\Tabletmanagerdata\SchemaDefinition $value){
      return $this->_set(2, $value);
    }
  }
}

